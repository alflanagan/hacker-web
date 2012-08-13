from django.db import models
from django.contrib.auth.models import User

"""
"
" Licensed under what is outlined in LICENSE in the application root 
" Purpose - To define the replationships for a hackerspace user
"
"""
class SpaceAllocations(models.Model):
    '''
    definable space allocations for projects
    for when space is tight
    '''

    name = models.CharField(max_length=32, help_text="Allocation Name")
    notes = models.TextField(null=True,blank=True,help_text="optional notes")

    def __unicode__(self):
        return self.name

class UserProjects(models.Model):
    '''
    representing user projects within the space
    '''
    
    name = models.CharField(max_length=32, help_text="a short name for your project")
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True, help_text="whether or not you are active within the space currently")
    space_requirement = models.ForeignKey(SpaceAllocations, null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    projected_completion_date = models.DateField(help_text="when do you think you will finish this project?")
    actual_completion_date = models.DateField(null=True, blank=True)
    description = models.TextField(help_text="a few words about your project")
    
    def __unicode__(self):
        return "%s-%s" %(self.name, str(self.user))

    @property
    def is_active(self):
        if self.active:
            return True
        else:
            return False

    @property
    def has_space(self):
        if self.space_requirements:
            return True
        else:
            return False 
