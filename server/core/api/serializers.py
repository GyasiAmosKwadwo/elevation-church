from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Sermon, Resource, Series, Event, Devotion, Reflection, Prayer_request, Announcement, Live_stream
from datetime import date
from django.urls import reverse
from django.contrib.auth import get_user_model


class BibleVerseSerializer(serializers.Serializer):
    reference = serializers.CharField(max_length=300, required=False, allow_blank=True, allow_null=True, help_text="Bible verse reference, e.g., 'John 10:30'")
    verse_content = serializers.CharField(required=False, allow_blank=True, allow_null=True, help_text="The content of the Bible verse")


class ReflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflection
        fields = ['id', 'name', 'likes', 'comments', 'content', 'devotion', 'date']
        read_only_fields = ['id', 'date']

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'purchase_link', 'price']
        read_only_fields = ['id']

class SermonSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)
    reflection = ReflectionSerializer(many=True, read_only=True)
    next_sermon = serializers.SerializerMethodField()
    previous_sermon = serializers.SerializerMethodField()

    class Meta:
        model = Sermon
        fields = [
            'id', 'title', 'description', 'preacher', 'video_link',
            'podcast_link', 'series', 'date', 'resources', 'likes','next_sermon', 'previous_sermon', 'reflection'
        ]
        read_only_fields = ['id', 'date', 'resources', 'next_sermon', 'previous_sermon']
        
    @extend_schema_field(serializers.URLField(allow_null=True))
    def get_next_sermon(self, obj):
        series = self.context.get('series')
        if not series:
            return None
        sermons = list(series.sermon_series.order_by('date'))
        try:
            index = sermons.index(obj)
            if index < len(sermons) - 1:
                next_obj = sermons[index + 1]
                request = self.context.get('request')
                if request:
                    return request.build_absolute_uri(reverse('sermon-detail', kwargs={'sermon_id': next_obj.id}))
                return reverse('sermon-detail', kwargs={'sermon_id': next_obj.id})
        except ValueError:
            pass
        return None

    @extend_schema_field(serializers.URLField(allow_null=True))
    def get_previous_sermon(self, obj):
        series = self.context.get('series')
        if not series:
            return None
        sermons = list(series.sermon_series.order_by('date'))
        try:
            index = sermons.index(obj)
            if index > 0:
                prev_obj = sermons[index - 1]
                request = self.context.get('request')
                if request:
                    return request.build_absolute_uri(reverse('sermon-detail', kwargs={'sermon_id': prev_obj.id}))
                return reverse('sermon-detail', kwargs={'sermon_id': prev_obj.id})
        except ValueError:
            pass
        return None

class SeriesSerializer(serializers.ModelSerializer):
    available_sermons = serializers.SerializerMethodField()
    class Meta:
        model = Series
        fields = ['id', 'title', 'description', 'image', 'thoughts','available_sermons']
        read_only_fields = ['id']

    def get_available_sermons(self, obj):
        sermons = obj.sermon_series.order_by('date')
        return SermonSerializer(sermons, many=True, context={'series': obj, 'request': self.context.get('request')}).data


class EventSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField()
    end_date = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id', 'name', 'description', 'flyer', 'location', 'date',
            'end_date', 'days', 'start_time', 'end_time', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'days', 'end_date']

    @extend_schema_field(serializers.IntegerField())
    def get_days(self, obj) -> int:
        return obj.days

    @extend_schema_field(serializers.DateField())
    def get_end_date(self, obj) -> 'date':
        from datetime import timedelta, date, datetime
        base_date = obj.date
      
        if isinstance(base_date, datetime):
            base_date = base_date.date()
        if base_date and obj.days:
            return base_date + timedelta(days=obj.days - 1)
        return None  # type: ignore
    


class DevotionSerializer(serializers.ModelSerializer):
    Bible_verse = serializers.JSONField(required=False, allow_null=True)
    reflections = ReflectionSerializer(many=True, read_only=True)
    thumbnail = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Devotion
        fields = ['id', 'title', 'Bible_verse', 'content', 'thumbnail', 'date', 'reflections']
        read_only_fields = ['id']

    def create(self, validated_data):
        bible = validated_data.pop('Bible_verse', {})
        bible = self.validate_Bible_verse(bible)
        return Devotion.objects.create(Bible_verse=bible, **validated_data)

    def update(self, instance, validated_data):
        bible = validated_data.pop('Bible_verse', None)
        if bible is not None:
            instance.Bible_verse = self.validate_Bible_verse(bible)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_Bible_verse(self, value):
        # Accept either a dict or a JSON string for Bible_verse
        if isinstance(value, str):
            import json
            try:
                value = json.loads(value)
            except json.JSONDecodeError as e:
                raise serializers.ValidationError(f"Invalid JSON for Bible_verse: {e}")
        if not isinstance(value, dict):
            raise serializers.ValidationError("Bible_verse must be an object with 'reference' and 'verse_content'.")
        # Ensure required keys
        value.setdefault('reference', '')
        value.setdefault('verse_content', '')
        return value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        import json
        bv = instance.Bible_verse
        if isinstance(bv, str):
            try:
                bv = json.loads(bv)
            except Exception:
                bv = {}
        if not isinstance(bv, dict):
            bv = {}
        data['Bible_verse'] = {
            'reference': bv.get('reference', ''),
            'verse_content': bv.get('verse_content', ''),
        }
        return data


class PrayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prayer_request
        fields = ['id', 'name', 'subject', 'date']
        read_only_fields = ['id', 'date']


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'content', 'date']
        read_only_fields = ['id', 'date']

class LiveStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live_stream
        fields = ['id', 'title', 'description', 'stream_link', 'status', 'reactions', 'comments', 'date']
        read_only_fields = ['id']


class StaffUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'is_staff', 'date_joined']
        read_only_fields = ['id', 'is_staff', 'date_joined']

    def create(self, validated_data):
        password = validated_data.pop('password')
        User = get_user_model()
        user = User(**validated_data)
        user.is_staff = True
        user.is_superuser = False
        user.set_password(password)
        user.save()
        return user


