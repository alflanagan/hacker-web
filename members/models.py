from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save, post_syncdb
from spaces.models import HackerSpace

"""
"
" Licensed under what is outlined in LICENSE in the application root 
" Purpose - To define the replationships for a hackerspace user
"
"""

class MemberInterests(models.Model):
    '''
    used to track what hackers are interested in
    '''
    name = models.CharField(max_length=32,unique=True,help_text="Name of this interest")
    notes = models.TextField(null=True,blank=True,help_text="Optional Notes")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Member Interests'

class MemberProfile(models.Model):
    '''
    extending the default User model
    '''

    user = models.OneToOneField(User)
    hackerspace = models.ForeignKey(HackerSpace, blank=True, null=True, help_text="the space the member belongs to")
    interests = models.ManyToManyField(MemberInterests, blank=True, null=True)
    rsa_key = models.TextField(null=True, blank=True, help_text="optional RSA Public Key")
    pgp_key = models.TextField(null=True, blank=True, help_text="optional PGP Key")
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/", help_text="optional avatar (jpg,gif,png)")

    def display_email(self):
        return self.user.email
    display_email.short_description = 'email'

    def is_trainer(self):
        g = Group.objects.get(name='Trainers')
        if g in self.user.groups.all():
            return True
        else:
            return False
    is_trainer.short_description = 'trainer'
    is_trainer.boolean = True

    def is_staff(self):
        return self.user.is_staff
    is_staff.short_description = 'member'
    is_staff.boolean = True

    def get_full_name(self):
        return str("%s %s") % (self.user.first_name, self.user.last_name)

    def __unicode__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Member Profile'

def create_member_profile(sender, instance, created, **kwargs):
    if created:
        MemberProfile.objects.create(user=instance)

post_save.connect(create_member_profile, sender=User)

