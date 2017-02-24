from django.contrib import admin
from equipment.models import HackerEquipment

class hackerEquipmentAdmin(admin.ModelAdmin):

    save_on_top = True

admin.site.register(HackerEquipment, hackerEquipmentAdmin)
