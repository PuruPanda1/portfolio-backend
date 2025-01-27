from django.contrib import admin
from .models import *

admin.site.register(HeroDetails)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)

class ProjectPhotoInline(admin.TabularInline):
    model = ProjectPhoto
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [ProjectPhotoInline]