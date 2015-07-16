from django.contrib import admin

from .models import Group, Record


class RecordInline(admin.TabularInline):
    model = Record
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'desc']}),
        ('Members', {'fields': ['members']}),
    ]
    inlines = [RecordInline]
    list_display = ('name', 'id', 'desc', 'creation_date', 'last_change_date')
    list_filter = ['creation_date']
    search_fields = ['name', 'desc']


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'id', 'amount', 'note',
                    'payer', 'receiver', 'creation_date', 'last_change_date')
    list_filter = ['creation_date', 'payer', 'receiver']
    search_fields = ['name', 'note']


admin.site.register(Group, GroupAdmin)
admin.site.register(Record, RecordAdmin)
