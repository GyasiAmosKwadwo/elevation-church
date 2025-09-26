from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Sermon, Resource, Series, Event
from datetime import date
from django.urls import reverse



class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'purchase_link', 'price']
        read_only_fields = ['id']

class SermonSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)
    next_sermon = serializers.SerializerMethodField()
    previous_sermon = serializers.SerializerMethodField()

    class Meta:
        model = Sermon
        fields = [
            'id', 'title', 'description', 'preacher', 'video_link',
            'podcast_link', 'series', 'date', 'resources', 'next_sermon', 'previous_sermon'
        ]
        read_only_fields = ['id', 'date', 'resources', 'next_sermon', 'previous_sermon']

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
        fields = ['id', 'title', 'description', 'image', 'available_sermons']
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
        # Ensure base_date is a date object
        if isinstance(base_date, datetime):
            base_date = base_date.date()
        if base_date and obj.days:
            return base_date + timedelta(days=obj.days - 1)
        return None  # type: ignore
