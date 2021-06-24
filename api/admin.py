from django.contrib import admin
from django.contrib.admin.decorators import register
from api.models import Organization, User

# Register your models here.
@register(Organization)
class OrgAdmin(admin.ModelAdmin):
    pass

@register(User)
class UserAdmin(admin.ModelAdmin):
    pass
