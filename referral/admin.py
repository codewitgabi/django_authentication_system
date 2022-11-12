from django.contrib import admin
from .models import ReferralNotification, Referral


class ReferralAdmin(admin.ModelAdmin):
	list_display = ("user", "referral_code")
	search_fields = ("user__username", "referral_code")
	readonly_fields = ("user",)
	
	
class ReferralNotificationAdmin(admin.ModelAdmin):
	list_display = ("user",)
	search_fields = ("user__username",)
	readonly_fields = ("user",)
	
	
admin.site.register(Referral, ReferralAdmin)
admin.site.register(
	ReferralNotification,
	ReferralNotificationAdmin
)