from django.db import models
from django.contrib.auth.models import User
from sponsors.models import Sponsor

class Workshop(models.Model):
    '''
    'defines workshops that the space can hold
    '''
    name = models.CharField(max_length=32, unique=True, help_text="name for the class")
    instructor = models.ForeignKey(User, related_name='instructor_user', help_text="person presenting the workshop")
    attendees = models.ManyToManyField(User, related_name='attendee_user', help_text="people taking the workshop")
    date = models.DateField(help_text="date workshop will occur")
    start_time = models.TimeField(help_text="workshop start time")
    end_time = models.TimeField(help_text="workshop end time")
    date_created = models.DateField(auto_now_add=True)
    sponsor = models.ForeignKey(Sponsor, null=True, blank=True)

    def __unicode__(self):
        return self.name

    @property
    def is_sponsored(self):
        if self.sponsor:
            return True
        else: 
            return False
