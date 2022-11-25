from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from apps.users.models import User

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = "__all__"
