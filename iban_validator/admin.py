from django.contrib import admin
from .models import IbanHistory

def delete_selected(modeladmin, request, queryset):
    """
    Custom action to delete selected items.
    """
    queryset.delete()
    modeladmin.message_user(request, "Selected items have been deleted.")

delete_selected.short_description = "Delete selected items"

@admin.register(IbanHistory)
class IbanHistoryAdmin(admin.ModelAdmin):
    list_display = ('iban', 'is_valid', 'timestamp')
    search_fields = ('iban',)   
    actions = [delete_selected]
