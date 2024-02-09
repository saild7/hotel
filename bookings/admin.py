from django.contrib import admin

from bookings.models import Guest


# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name','email','phone','address']
    readonly_fields=['first_name', 'last_name','email','phone','address','country']
    can_delete=False

admin.site.register(Guest,GuestAdmin)
