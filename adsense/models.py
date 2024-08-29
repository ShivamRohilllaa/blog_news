from django.db import models

class GoogleAdSense(models.Model):
    ad_client = models.CharField(max_length=100, help_text="Your Google AdSense client ID (e.g., ca-pub-XXXXXXXXXXXXXXX)")
    ad_slot = models.CharField(max_length=100, help_text="Your Google AdSense ad slot ID (e.g., 1234567890)")
    ad_format = models.CharField(max_length=100, choices=[
        ('auto', 'Auto'),
        ('responsive', 'Responsive'),
        ('fixed', 'Fixed'),
    ], default='auto', help_text="Format of the AdSense ad (e.g., Auto, Responsive, Fixed)")
    is_active = models.BooleanField(default=True, help_text="Toggle to activate or deactivate this ad.")
    description = models.CharField(max_length=255, blank=True, null=True, help_text="A short description for internal reference.")

    def __str__(self):
        return f"Ad: {self.ad_client} - Slot: {self.ad_slot}"

    class Meta:
        verbose_name = "Google AdSense"
        verbose_name_plural = "Google AdSense Ads"
