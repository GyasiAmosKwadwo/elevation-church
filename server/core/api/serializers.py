from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from django.utils import timezone
from decimal import Decimal
from .models import (
    Sermon,
    Resource,
    Series,
    Event,
    Devotion,
    Reflection,
    Prayer_request,
    Announcement,
    Live_stream,
    Gallery,
    GalleryImage,
    ContributionChannel,
    ContributionIntent,
    Reel,
    SiteSettings,
    ThemeSettings,
    NavigationItem,
    PageConfig,
    SectionConfig,
)
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
    resource_details = ResourceSerializer(source='resource', read_only=True)
    next_sermon = serializers.SerializerMethodField()
    previous_sermon = serializers.SerializerMethodField()

    class Meta:
        model = Sermon
        fields = [
            'id', 'title', 'description', 'preacher', 'video_link',
            'podcast_link', 'series', 'resource', 'resource_details', 'date',
            'likes', 'comments', 'next_sermon', 'previous_sermon'
        ]
        read_only_fields = ['id', 'date', 'resource_details', 'next_sermon', 'previous_sermon']
        
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
        fields = ['id', 'title', 'description', 'image', 'thoughts', 'available_sermons']
        read_only_fields = ['id']

    def get_available_sermons(self, obj):
        sermons = obj.sermon_series.order_by('date')
        return SermonSerializer(sermons, many=True, context={'series': obj, 'request': self.context.get('request')}).data


class EventSerializer(serializers.ModelSerializer):
    days = serializers.IntegerField(required=False, min_value=1)
    end_date = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id', 'name', 'description', 'flyer', 'location', 'date',
            'end_date', 'days', 'start_time', 'end_time', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'end_date']

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
    thumbnail = serializers.URLField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Devotion
        fields = ['id', 'title', 'Bible_verse', 'content', 'thumbnail', 'date', 'reflections']
        read_only_fields = ['id', 'date', 'reflections']

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
        fields = ['id', 'name', 'phone_contact', 'subject', 'date']
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

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'gallery', 'title', 'image', 'description', 'venue', 'likes', 'date']
        read_only_fields = ['id', 'date']


class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)
    image_urls = serializers.ListField(
        child=serializers.URLField(),
        write_only=True,
        required=False,
        allow_empty=True
    )

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'description', 'venue', 'likes', 'date', 'images', 'image_urls']
        read_only_fields = ['id', 'date', 'images']

    def create(self, validated_data):
        image_urls = validated_data.pop('image_urls', [])
        gallery = super().create(validated_data)
        for index, url in enumerate(image_urls, start=1):
            GalleryImage.objects.create(
                gallery=gallery,
                title=f"{gallery.title} - Image {index}",
                image=url,
                description=gallery.description,
                venue=gallery.venue,
            )
        return gallery

    def update(self, instance, validated_data):
        image_urls = validated_data.pop('image_urls', None)
        gallery = super().update(instance, validated_data)

        if image_urls is not None:
            existing = gallery.images.count()
            for offset, url in enumerate(image_urls, start=1):
                GalleryImage.objects.create(
                    gallery=gallery,
                    title=f"{gallery.title} - Image {existing + offset}",
                    image=url,
                    description=gallery.description,
                    venue=gallery.venue,
                )

        return gallery


class ContributionChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributionChannel
        fields = [
            'id', 'name', 'channel_type', 'account_name', 'account_number',
            'bank_name', 'branch', 'network', 'currency', 'instructions',
            'is_active', 'display_order', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ContributionIntentSerializer(serializers.ModelSerializer):
    channel_details = ContributionChannelSerializer(source='channel', read_only=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=Decimal('0.01'))
    confirmed_by = serializers.SerializerMethodField()

    class Meta:
        model = ContributionIntent
        fields = [
            'id', 'channel', 'channel_details', 'amount', 'purpose', 'donor_name',
            'donor_phone', 'reference', 'proof_url', 'status', 'admin_note',
            'confirmed_by', 'confirmed_at', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'channel_details', 'confirmed_by', 'confirmed_at', 'created_at', 'updated_at']

    @extend_schema_field(serializers.CharField(allow_null=True))
    def get_confirmed_by(self, obj):
        if not obj.confirmed_by:
            return None
        return obj.confirmed_by.username

    def create(self, validated_data):
        validated_data['status'] = 'pending'
        validated_data['confirmed_by'] = None
        validated_data['confirmed_at'] = None
        validated_data['admin_note'] = ''
        return super().create(validated_data)

    def update(self, instance, validated_data):
        old_status = instance.status
        instance = super().update(instance, validated_data)
        request = self.context.get('request')
        new_status = instance.status

        if new_status == 'confirmed':
            if old_status != 'confirmed' or not instance.confirmed_at:
                instance.confirmed_at = timezone.now()
                if request and request.user and request.user.is_authenticated:
                    instance.confirmed_by = request.user
                instance.save(update_fields=['confirmed_at', 'confirmed_by'])
        elif old_status == 'confirmed' and new_status != 'confirmed':
            instance.confirmed_at = None
            instance.confirmed_by = None
            instance.save(update_fields=['confirmed_at', 'confirmed_by'])

        return instance


class ReelSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Reel
        fields = [
            'id', 'title', 'caption', 'video_url', 'thumbnail_url', 'category',
            'is_published', 'published_at', 'views_count', 'likes_count',
            'created_by', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'published_at', 'views_count', 'likes_count', 'created_by', 'created_at', 'updated_at']

    @extend_schema_field(serializers.CharField(allow_null=True))
    def get_created_by(self, obj):
        if not obj.created_by:
            return None
        return obj.created_by.username

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            validated_data['created_by'] = request.user
        if validated_data.get('is_published', True):
            validated_data.setdefault('published_at', timezone.now())
        return super().create(validated_data)

    def update(self, instance, validated_data):
        old_published = instance.is_published
        instance = super().update(instance, validated_data)
        new_published = instance.is_published

        if new_published and (not old_published) and not instance.published_at:
            instance.published_at = timezone.now()
            instance.save(update_fields=['published_at'])
        elif not new_published:
            instance.published_at = None
            instance.save(update_fields=['published_at'])

        return instance


class SiteSettingsSerializer(serializers.ModelSerializer):
    service_times = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
    )
    social_links = serializers.DictField(
        child=serializers.URLField(),
        required=False,
    )

    class Meta:
        model = SiteSettings
        fields = [
            'id', 'church_name', 'tagline', 'logo_url', 'banner_image_url',
            'phone', 'email', 'address', 'service_times', 'social_links',
            'footer_note', 'default_seo_title', 'default_seo_description',
            'default_og_image_url', 'show_announcements', 'show_gallery',
            'show_resources', 'show_prayer_request', 'show_live_badge',
            'updated_at',
        ]
        read_only_fields = ['id', 'updated_at']


class ThemeSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeSettings
        fields = [
            'id', 'primary_color', 'secondary_color', 'accent_color',
            'text_color', 'background_color', 'border_color',
            'heading_font', 'body_font', 'button_style', 'card_radius',
            'button_radius', 'shadow_strength', 'layout_density',
            'section_spacing', 'dark_mode_enabled', 'updated_at',
        ]
        read_only_fields = ['id', 'updated_at']


class NavigationItemSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = NavigationItem
        fields = [
            'id', 'label', 'url', 'item_type', 'parent', 'location',
            'display_order', 'is_enabled', 'open_in_new_tab', 'cta_style',
            'children', 'updated_at',
        ]
        read_only_fields = ['id', 'children', 'updated_at']

    def get_children(self, obj):
        queryset = obj.children.filter(is_enabled=True).order_by('display_order', 'label')
        return [
            {
                'id': child.id,
                'label': child.label,
                'url': child.url,
                'item_type': child.item_type,
                'location': child.location,
                'display_order': child.display_order,
                'open_in_new_tab': child.open_in_new_tab,
                'cta_style': child.cta_style,
            }
            for child in queryset
        ]

    def validate(self, attrs):
        item_type = attrs.get('item_type', getattr(self.instance, 'item_type', 'link'))
        url = attrs.get('url', getattr(self.instance, 'url', ''))
        parent = attrs.get('parent', getattr(self.instance, 'parent', None))
        location = attrs.get('location', getattr(self.instance, 'location', 'header'))

        if item_type == 'link' and not url:
            raise serializers.ValidationError({'url': 'URL is required for link items.'})
        if parent:
            if self.instance and parent.pk == self.instance.pk:
                raise serializers.ValidationError({'parent': 'An item cannot be its own parent.'})
            if parent.location != location:
                raise serializers.ValidationError({'parent': 'Parent and child must share the same location.'})
        return attrs


class SectionConfigSerializer(serializers.ModelSerializer):
    page_slug = serializers.CharField(source='page.slug', read_only=True)

    class Meta:
        model = SectionConfig
        fields = [
            'id', 'page', 'page_slug', 'key', 'title', 'subtitle', 'body',
            'cta_label', 'cta_url', 'background_image_url', 'overlay_opacity',
            'text_align', 'is_enabled', 'display_order', 'extra', 'updated_at',
        ]
        read_only_fields = ['id', 'page_slug', 'updated_at']


class PageConfigSerializer(serializers.ModelSerializer):
    sections = SectionConfigSerializer(many=True, read_only=True)

    class Meta:
        model = PageConfig
        fields = [
            'slug', 'title', 'subtitle', 'body', 'hero_image_url',
            'seo_title', 'seo_description', 'is_enabled', 'display_order',
            'updated_at', 'sections',
        ]
        read_only_fields = ['updated_at', 'sections']
