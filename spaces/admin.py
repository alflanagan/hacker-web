from django.contrib import admin
from spaces.models import HackerSpace, Locations

class HackerSpaceAdmin(admin.ModelAdmin):

    save_on_top = True

class LocationsAdmin(admin.ModelAdmin):

    save_on_top = True

admin.site.register(HackerSpace, HackerSpaceAdmin)
admin.site.register(Locations, LocationsAdmin)
