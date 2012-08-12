from django import forms
from members.models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
