from django.contrib import admin
from .models import Mysee
# Register your models here.
class MyseeAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email']

admin.site.register(Mysee, MyseeAdmin)