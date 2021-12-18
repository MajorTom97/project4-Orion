from django.contrib import admin
from .models import AstroPost, News, Video
from embed_video.admin import AdminVideoMixin


# Register your models here.

admin.site.register(News)
admin.site.register(AstroPost)



class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, MyModelAdmin)