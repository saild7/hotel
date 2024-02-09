from django.contrib import admin

import admin_thumbnails
from room.models import Images, Room

# Register your models here.


@admin_thumbnails.thumbnail('image')
class RoomImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_thumbnail']  

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','price', 'status','image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)
    inlines = [RoomImageInline]
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Room,RoomAdmin)
admin.site.register(Images,ImagesAdmin)
