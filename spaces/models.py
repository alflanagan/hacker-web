from django.db import models

class HackerSpace(models.Model):
    '''
    The hackerspace object represents a singular hackerspace entity. It's
    physical presence in the world. It essentially maintains the
    address/geo/lab names/etc. for a given hackerspace
    '''
    name = models.CharField(max_length=64, help_text="the name for your hacker or maker space")
    slogan = models.CharField(max_length=256, blank=True, null=True, help_text="an optional slogan to show up on your pages for your hackerspace")
    logo = models.ImageField(upload_to='logos/', height_field='logo_height', width_field='logo_width', blank=True, null=True, help_text="an optional logo for your hackerspace")
    address1 = models.CharField(max_length=96, help_text="the address for your hackerspace")
    address2 = models.CharField(max_length=96, null=True, blank=True, help_text="2nd optional address line")
    city = models.CharField(max_length=64, help_text="city")
    state = models.CharField(max_length=2, help_text="state")
    zip_code = models.CharField(max_length=16, help_text="zip/postal code")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Hacker Space'

class Locations(models.Model):
    '''
    This model represents areas inside and under the control of the hackerspace
    '''
    name = models.CharField(max_length=32, help_text='the name for this location')
    space = models.ForeignKey(HackerSpace, help_text='the space this location is associated with')
    notes = models.TextField(null=True, blank=True, help_text='optional notes')
