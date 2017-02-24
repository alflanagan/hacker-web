"""Equipment used by hackers, kept at the space, etc."""
from django.db import models
from django.contrib.auth.models import User
from spaces.models import Locations

class HackerEquipment(models.Model):
    '''
    This class represents equipment available in the hackerspace for use
    '''

    name = models.CharField(max_length=64, unique=True,
                            help_text='a common name for this piece of equipment')
    manufacturer = models.CharField(max_length=64, help_text='the equipment manufacturer')
    equipment_model = models.CharField(max_length=32, verbose_name='model',
                                       help_text='the model for this equipment')
    peramanent_owner = models.ForeignKey(User, null=True, blank=True,
                                         help_text=('if on loan from someone, who does this'
                                                    ' belong to permanently?'))
    value = models.IntegerField(help_text='fair market value')
    location = models.ForeignKey(Locations, help_text='location of equipment')
    notes = models.TextField(null=True, blank=True, help_text='Optional Notes')
