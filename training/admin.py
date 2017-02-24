# pylint: disable=missing-docstring
from django.contrib import admin
from training.models import TrainingManual

class TrainingManualAdmin(admin.ModelAdmin):

    save_on_top = True

admin.site.register(TrainingManual, TrainingManualAdmin)
