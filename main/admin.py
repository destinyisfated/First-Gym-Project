from django.contrib import admin
from . import models
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display=('title', 'image_tag')
admin.site.register(models.Service, ServiceAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display=('title', 'image_tag')
admin.site.register(models.Gallery, GalleryAdmin)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display=('alt_text', 'image_tag')
admin.site.register(models.GalleryImage, GalleryImageAdmin)

class SubplanAdmin(admin.ModelAdmin):
    list_display=('title', 'price','highlited')
    list_editable=('highlited',)
admin.site.register(models.Subplan, SubplanAdmin)

class SubplanFeaturesAdmin(admin.ModelAdmin):
    list_display=('title',)
admin.site.register(models.SubplanFeatures, SubplanFeaturesAdmin)


class TrainerAdmin(admin.ModelAdmin):
    list_display=('fullname', 'username')
admin.site.register(models.Trainer, TrainerAdmin)

class SessionAdmin(admin.ModelAdmin):
    list_display=('title', 'description','image_tag')
admin.site.register(models.Session, SessionAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display=('trainer', '','image_tag')