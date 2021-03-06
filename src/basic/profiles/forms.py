from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from src.basic.profiles.models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile


ServiceFormSet  = inlineformset_factory(Profile, Service)
LinkFormSet     = inlineformset_factory(Profile, Link)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')