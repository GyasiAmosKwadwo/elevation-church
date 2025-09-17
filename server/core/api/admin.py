from django.contrib import admin
from .models import Sermon, Resource, Series, Event

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'preacher', 'series', 'resource', 'date')
    search_fields = ('title', 'preacher', 'description')
    list_filter = ('series', 'preacher', 'date')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('sermon',)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    list_filter = ('date',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date', 'days')
    search_fields = ('name', 'location', 'description')
    list_filter = ('date', 'location')