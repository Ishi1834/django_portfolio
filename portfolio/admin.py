from django.contrib import admin
from .models import Project, TechStack, Resume, Certificate

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ['name', 'description']

admin.site.register(Project, ProjectAdmin)
admin.site.register(TechStack)
admin.site.register(Resume)
admin.site.register(Certificate)