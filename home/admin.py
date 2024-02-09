from django.contrib import admin

from home.models import ContactMessage, Setting


# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display=['title','hotel','update_at','status']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display=['name','subject','update_at','status'] 
    readonly_fields=('name','subject','email','message') 
    list_filter=['status']

admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)
