from django.db import models
from django.contrib.auth.models import User
from equipment.models import hackerEquipment

class TrainingManual(models.Model):
    '''
    a "training manual" is an information set that represents who is responsible for training new users on equipment as well as normally a document attachement that can be printed for reference. For some of the more straightforward equipment, however, (e.g. drill press), a verbal introduction is all that is required.
    '''

    name = models.CharField(max_length=32, unique=True, help_text='name for this manual')
    equipment = models.ForeignKey(hackerEquipment, help_text='equipment this manual is for')
    maintainer = models.ForeignKey(User, help_text='person who maintains this manual')
    training_time = models.IntegerField(max_length=4, help_text='approximate time in minutes training will take to complete')
    training_docs = models.FileField(upload_to='manuals/', null=True, blank=True, help_text='optional documentation that can be printed')
    notes = models.TextField(null=True, blank=True, help_text='optional notes')

