from django.contrib import admin
from django.contrib.admin.decorators import register
from api.models import Organization

# Register your models here.
@register(Organization)
class OrgAdmin(admin.ModelAdmin):
    pass

