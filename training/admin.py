from django.contrib import admin
from training.models import trainingManual

class trainingManualAdmin(admin.ModelAdmin):

    save_on_top = True

admin.site.register(trainingManual, trainingManualAdmin)
