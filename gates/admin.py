from django.contrib import admin

from .models import Group, Cost


class CostInline(admin.TabularInline):
    model = Cost
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'desc']}),
        ('Members', {'fields': ['members']}),
    ]
    inlines = [CostInline]
    list_display = ('name', 'id', 'desc', 'creation_date', 'last_change_date')
    list_filter = ['creation_date']
    search_fields = ['name', 'desc']


class CostAdmin(admin.ModelAdmin):
    # TODO: fix receiver
    list_display = ('name', 'group', 'id', 'amount', 'note',
                    'payer', 'creation_date', 'last_change_date')
    list_filter = ['creation_date', 'payer', 'receiver']
    search_fields = ['name', 'note']


admin.site.register(Group, GroupAdmin)
admin.site.register(Cost, CostAdmin)
