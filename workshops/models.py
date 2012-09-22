from django.db import models
from django.contrib.auth.models import User

class WorkshopCategory(models.Model):

    name = models.CharField(max_length=32, unique=True, help_text="name for this category")
    description = models.TextField(blank=True, null=True, help_text="optional notes")

class Workshop(models.Model):
    '''
    'defines workshops that the space can hold
    '''
    name = models.CharField(max_length=32, unique=True, help_text="name for the workshop")
    category = models.ForeignKey(ModelCategory, help_text="category this workshop falls under")
    number = models.CharField(max_length=4, help_text="number for class. e.g. 101, 500, etc.")
    instructor = models.ForeignKey(User, help_text="person presenting the workshop")
    date = models.DateField(help_text="date workshop will occur")
    start_time = models.TimeField(help_text="workshop start time")
    end_time = models.TimeField(help_text="workshop end time")
    date_created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s %s-%s" % (self.category.name, self.number, self.name)


