from django.contrib import admin
from workshops.models import WorkshopCategory, Workshop

class WorkshopAdmin(admin.ModelAdmin):

    save_on_top = True

class WorkshopCategoryAdmin(admin.ModelAdmin):

    save_on_top = True

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(WorkshopCategory, WorkshopCategoryAdmin)
