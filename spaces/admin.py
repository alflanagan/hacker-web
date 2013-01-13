from django.contrib import admin
from spaces.models import HackerSpace

class HackerSpaceAdmin(admin.ModelAdmin):

    save_on_top = True

admin.site.register(HackerSpace, HackerSpaceAdmin)
