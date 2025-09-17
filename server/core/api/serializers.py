from rest_framework import serializers
from .models import Sermon, Resource, Series, Event

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

    def get_days(self, obj):
        return obj.days

    def get_end_date(self, obj):
        if obj.date and obj.days:
            from datetime import timedelta
            return obj.date + timedelta(days=obj.days - 1)
        return None