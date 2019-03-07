from django.contrib import admin
from .models import *
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
      list_display = ('name', 'reason', 'anger_procent', 'date')
admin.site.register(Item, ItemAdmin)
admin.site.register(Offender)
