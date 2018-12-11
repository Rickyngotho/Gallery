from django.contrib import admin
from .models import Editor,pic,tags
# Register your models here.

class PicAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(pic,PicAdmin)
admin.site.register(tags)