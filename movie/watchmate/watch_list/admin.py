from django.contrib import admin

from .models import WatchList, StreamPlatform, Review


# Register your models here.


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ['title', 'platform', 'num_rating', 'avg_rating', 'active']
    ordering = ['title']
    list_filter = ['platform','created', 'avg_rating']
    search_fields = ['title', 'description']
    date_hierarchy = 'created'
    list_display_links = ['title', 'platform']


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'website']
    ordering = ['name']
    list_filter = ['name', 'website']
    search_fields = ['name', 'about', 'website']
    # list_editable = ['name', 'website']
    list_display_links = ['name', 'website']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['reviewer', 'watchlist', 'rating', 'active']
    ordering = ['reviewer']
    list_filter = ['rating', 'active', 'created']
    search_fields = ['reviewer__username', 'reviewer__review__description', 'description', 'watchlist__title']
    list_display_links = ['reviewer', 'watchlist']
