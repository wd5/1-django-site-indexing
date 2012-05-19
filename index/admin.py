from index.models import Site, Page
from django.contrib import admin

class SiteAdmin(admin.ModelAdmin):
    actions = ('reset_stats',)
    list_display = ('name', 'views', 'clicks')
    fieldsets = (
        ('Site Information', {
            'fields': ('name', 'url', 'tags', 'description')
        }),
        ('Analytics', {
            'classes': ('collapse',),
            'fields': ('views', 'clicks')
        }),
    )
    
    def reset_stats(self, request, queryset):
        queryset.update(clicks=0, views=0)
    reset_stats.short_description = "Reset stats on selected sites"

class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    fieldsets = (
        ('Page Information', {
            'fields': ('name', 'order', 'slug', 'tags')
        }),
        ('Content', {
            'fields': ('body',)
        }),
    )
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(Site, SiteAdmin)
admin.site.register(Page, PageAdmin)
