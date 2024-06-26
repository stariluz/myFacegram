from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('pk','user', 'phone_number', 'description','picture')

    list_display_links=('pk','user')

    list_editable=('phone_number',)

    search_fields=('user__email','user__first_name', 'user__last_name', 'phone_number')
    
    fieldsets=(
        ('Profile',{
            'fields': ('user','picture')
        }),
        ('Information',{
            'fields':(
                ('phone_number'),
                ('description')
            )
        }),
        ('Metadata',{
            'fields':(
                ('created','modified'),
            ),
        })
    )

    readonly_fields=(
        'created',
        'modified',
    )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete=False
    verbose_name_plural='profiles'

class UserAdmin(BaseUserAdmin):
    inlines=(ProfileInline,)
    list_display=(
        'pk',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff', 
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)