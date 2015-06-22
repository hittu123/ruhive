from django import forms

from src.basic.invitations import Invitation


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        exclude = ('status', 'from_user', 'site', 'token')
