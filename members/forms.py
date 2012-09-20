from django import forms
from members.models import MemberProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
