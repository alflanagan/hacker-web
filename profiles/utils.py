"""
Utility functions for retrieving and generating forms for the
site-specific user profile model specified in the
``AUTH_PROFILE_MODULE`` setting.

"""

from django import forms
from django.conf import settings
from django.contrib.auth.models import SiteProfileNotAvailable
from django.db.models import get_model
from django.contrib.auth.models import User
from members.models import UserProfile
from members.forms import ProfileForm

def get_profile_model():
    """
    Return the model class for the currently-active user profile
    model, as defined by the ``AUTH_PROFILE_MODULE`` setting. If that
    setting is missing, raise
    ``django.contrib.auth.models.SiteProfileNotAvailable``.
    
    """
    if (not hasattr(settings, 'AUTH_PROFILE_MODULE')) or \
           (not settings.AUTH_PROFILE_MODULE):
        raise SiteProfileNotAvailable
    profile_mod = get_model(*settings.AUTH_PROFILE_MODULE.split('.'))
    if profile_mod is None:
        raise SiteProfileNotAvailable
    return profile_mod

class ProfileForm(forms.ModelForm):

    #profile_mod = get_profile_model()


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        try:
            self.fields['email'].initial = self.instance.user.email
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name

        except User.DoesNotExist:
            pass

    email = forms.EmailField(label="Primary email",help_text='')
    first_name = forms.CharField(max_length=32, label="First Name", help_text='')
    last_name = forms.CharField(max_length=32, label="Last Name", help_text='')

    class Meta:
        model = UserProfile
        exclude = ('user','points','is_student','is_teacher', 'friends','accepted_eula')

    def save(self, *args, **kwargs):
        """
        Update the primary email address on the related User object as well.
        """
        u = self.instance.user
        u.email = self.cleaned_data['email']
        u.first_name = self.cleaned_data['first_name']
        u.last_name = self.cleaned_data['last_name']
        u.save()

        profile = super(ProfileForm, self).save(*args,**kwargs)

        return profile

def get_profile_form():
    """
    Return a form class (a subclass of the default ``ModelForm``)
    suitable for creating/editing instances of the site-specific user
    profile model, as defined by the ``AUTH_PROFILE_MODULE``
    setting. If that setting is missing, raise
    ``django.contrib.auth.models.SiteProfileNotAvailable``.
    
    """
    #profile_mod = get_profile_model()
    
    return ProfileForm

