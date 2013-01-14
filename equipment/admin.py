from django.contrib import admin
from equipment.models import hackerEquipment

class hackerEquipmentAdmin(admin.ModelAdmin):

    save_on_top = True

admin.site.register(hackerEquipment, hackerEquipmentAdmin)
