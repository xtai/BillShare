from django.contrib import admin

from .models import Group, Record


class RecordInline(admin.TabularInline):
    model = Record
    extra = 1

<<<<<<< HEAD

class ProjectAdmin(admin.ModelAdmin):
=======
class GroupAdmin(admin.ModelAdmin):
>>>>>>> b30bd39e38faf08a11245cea28f5001676457fc2
    fieldsets = [
        (None, {'fields': ['name', 'desc']}),
        ('Members', {'fields': ['members']}),
        ('Creation Date', {'fields': ['creation_date']}),
    ]
    inlines = [RecordInline]
    list_display = ('name', 'id', 'desc', 'creation_date', 'last_change_date')
    list_filter = ['creation_date']
    search_fields = ['name', 'desc']


<<<<<<< HEAD
class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'id', 'amount', 'note',
                    'payer', 'receiver', 'creation_date', 'last_change_date')
    list_filter = ['creation_date', 'payer', 'receiver']
    search_fields = ['name', 'note']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Record, RecordAdmin)
=======
admin.site.register(Group, GroupAdmin)
admin.site.register(Record)
>>>>>>> b30bd39e38faf08a11245cea28f5001676457fc2
