from django.contrib import admin
from .models import Sermon, Resource, Series, Event, Devotion, Reflection, Prayer_request, Announcement

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'preacher', 'resource', 'date')
    search_fields = ('title', 'preacher', 'description')
    list_filter = ('preacher', 'date')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('sermon',)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date', 'days')
    search_fields = ('name', 'location', 'description')
    list_filter = ('date', 'location')

@admin.register(Devotion)
class DevotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'Bible_verse', 'date')
    search_fields = ('title', 'Bible_verse', 'content')
    list_filter = ('date',)


@admin.register(Reflection)
class ReflectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'likes', 'date')
    search_fields = ('name', 'content', 'comments')
    list_filter = ('date', 'likes')

@admin.register(Prayer_request)
class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date')
    search_fields = ('name', 'subject')
    list_filter = ('date',)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'content')
    list_filter = ('date',)