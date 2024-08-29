from django.contrib import admin
from adsense.models import GoogleAdSense

@admin.register(GoogleAdSense)
class GoogleAdSenseAdmin(admin.ModelAdmin):
    list_display = ('ad_client', 'ad_slot', 'ad_format', 'is_active', 'description')
    list_filter = ('ad_format', 'is_active')
    search_fields = ('ad_client', 'ad_slot', 'description')
