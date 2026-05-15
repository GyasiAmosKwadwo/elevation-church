from django.contrib import admin
from .models import (
    Sermon,
    Resource,
    Series,
    Event,
    Devotion,
    Reflection,
    Prayer_request,
    Announcement,
    Gallery,
    GalleryImage,
    Live_stream,
    ContributionChannel,
    ContributionIntent,
    Reel,
    SiteSettings,
    ThemeSettings,
    NavigationItem,
    PageConfig,
    SectionConfig,
)

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
    list_display = ('name', 'phone_contact', 'subject', 'date')
    search_fields = ('name', 'phone_contact', 'subject')
    list_filter = ('date',)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'content')
    list_filter = ('date',)

@admin.register(Live_stream)
class LiveStreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date')
    search_fields = ('title', 'description')
    list_filter = ('status', 'date')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'gallery', 'date')
    search_fields = ('title', 'description', 'gallery__title')
    list_filter = ('date', 'gallery')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'likes', 'date')
    search_fields = ('title', 'description', 'venue')
    list_filter = ('date',)


@admin.register(ContributionChannel)
class ContributionChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'channel_type', 'account_name', 'account_number', 'is_active', 'display_order')
    search_fields = ('name', 'account_name', 'account_number', 'bank_name', 'network')
    list_filter = ('channel_type', 'is_active', 'currency')
    ordering = ('display_order', 'name')


@admin.register(ContributionIntent)
class ContributionIntentAdmin(admin.ModelAdmin):
    list_display = ('channel', 'amount', 'purpose', 'status', 'donor_name', 'created_at', 'confirmed_by')
    search_fields = ('donor_name', 'donor_phone', 'reference', 'channel__name')
    list_filter = ('status', 'purpose', 'channel__channel_type', 'created_at')
    autocomplete_fields = ('channel', 'confirmed_by')
    ordering = ('-created_at',)


@admin.register(Reel)
class ReelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'published_at', 'created_by', 'created_at')
    search_fields = ('title', 'caption', 'category')
    list_filter = ('is_published', 'category', 'created_at')
    ordering = ('-published_at', '-created_at')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('church_name', 'email', 'phone', 'updated_at')
    readonly_fields = ('updated_at',)


@admin.register(ThemeSettings)
class ThemeSettingsAdmin(admin.ModelAdmin):
    list_display = ('primary_color', 'secondary_color', 'accent_color', 'updated_at')
    readonly_fields = ('updated_at',)


@admin.register(NavigationItem)
class NavigationItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'location', 'item_type', 'parent', 'display_order', 'is_enabled')
    list_filter = ('location', 'item_type', 'is_enabled', 'cta_style')
    search_fields = ('label', 'url')
    ordering = ('location', 'display_order', 'label')


@admin.register(PageConfig)
class PageConfigAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'is_enabled', 'display_order', 'updated_at')
    list_filter = ('is_enabled',)
    search_fields = ('slug', 'title', 'subtitle')
    ordering = ('display_order', 'slug')


@admin.register(SectionConfig)
class SectionConfigAdmin(admin.ModelAdmin):
    list_display = ('key', 'page', 'title', 'is_enabled', 'display_order', 'updated_at')
    list_filter = ('is_enabled', 'text_align', 'page')
    search_fields = ('key', 'title', 'subtitle', 'page__slug')
    ordering = ('page__slug', 'display_order', 'key')
