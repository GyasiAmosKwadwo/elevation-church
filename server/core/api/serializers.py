from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Sermon, Resource, Series, Event
from datetime import date



class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'purchase_link', 'price']
        read_only_fields = ['id']

class SermonSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = Sermon
        fields = [
            'id', 'title', 'description', 'preacher', 'video_link',
            'podcast_link', 'date', 'series', 'resources'
        ]
        read_only_fields = ['id', 'date', 'resources']

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['id', 'title', 'description', 'image', 'date']
        read_only_fields = ['id', 'date']

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
