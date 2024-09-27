from django.contrib import admin

from .models import User

from modeltranslation.admin import TranslationAdmin
from adminsortable2.admin import SortableAdminMixin
@admin.register(User)
class UserAdmin(SortableAdminMixin, TranslationAdmin, admin.ModelAdmin):
    group_fieldsets= True
    list_display = ("name", "social_status", "school", "my_order")
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
# Register your models here.