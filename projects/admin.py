from django.contrib import admin
from projects.models import SpaceAllocations, UserProjects

class SpaceAllocationsAdmin(admin.ModelAdmin):

    save_on_top = True

class UserProjectsAdmin(admin.ModelAdmin):

    save_on_top = True
    readonly_fields = ('start_date','actual_completion_date')

admin.site.register(SpaceAllocations, SpaceAllocationsAdmin)
admin.site.register(UserProjects, UserProjectsAdmin)
