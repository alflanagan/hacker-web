from django.db import models
from django.contrib.auth.models import User

class WorkshopCategory(models.Model):

    name = models.CharField(max_length=32, unique=True, help_text="name for this category")
    description = models.TextField(blank=True, null=True, help_text="optional notes")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Workshop Category'
        verbose_name_plural = 'Workshop Categories'

class Workshop(models.Model):
    '''
    'defines workshops that the space can hold
    '''
    name = models.CharField(max_length=32, unique=True, help_text="name for the workshop")
    category = models.ForeignKey(WorkshopCategory, help_text="category this workshop falls under")
    number = models.CharField(max_length=4, help_text="number for class. e.g. 101, 500, etc.")
    instructor = models.ForeignKey(User, help_text="person presenting the workshop")
    date = models.DateField(help_text="date workshop will occur")
    start_time = models.TimeField(help_text="workshop start time")
    end_time = models.TimeField(help_text="workshop end time")
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField(help_text="description for your workshop")
    attendees = models.ManyToManyField(User, related_name="user_attendees", help_text="people attending this workshop")

    def __unicode__(self):
        return "%s %s-%s" % (self.category.name, self.number, self.name)
