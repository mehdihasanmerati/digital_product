from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .models import User, Province


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'phone_number', 'email')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('username', 'phone_number', 'password1', 'password2'),
                }),
    )
    list_display = ('username', 'phone_number', 'email', 'is_staff')
    search_fields = ('username_exact',)
    ordering = ('-id',)

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(request, queryset, search_term,)
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(phone_number=search_term_as_int)
        return queryset, may_have_duplicates


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_valid', 'modified_at', 'created_at']
    list_filter = ['id']
    search_fields = ['name']


admin.site.unregister(Group)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(User, MyUserAdmin)
