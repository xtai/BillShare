from django.contrib import admin

from .models import Project, Record


class RecordInline(admin.TabularInline):
    model = Record
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'desc']}),
        ('Members', {'fields': ['members']}),
        ('Creation Date', {'fields': ['creation_date']}),
    ]
    inlines = [RecordInline]
    list_display = ('name', 'desc', 'creation_date', 'last_change_date')
    list_filter = ['creation_date']
    search_fields = ['name', 'desc']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Record)
