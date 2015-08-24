from django import forms
from main.models import SpeedModel, CustomUser

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

        def __init__(self, *args, **kwargs):
                super(CustomUserCreationForm, self).__init__(*args, **kwargs)
                del self.fields['username']

        class Meta:
                model = CustomUser
                fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

        def __init__(self, *args, **kwargs):
                super(CustomUserChangeForm, self).__init__(*args, **kwargs)
                del self.fields['username']

        class Meta:
                model = CustomUser
                fields = '__all__'


class SpeedModelForm(forms.ModelForm):
        class Meta:
                model = SpeedModel
                fields = '__all__'


class SpeedModelForm2(forms.Form):
        title = forms.CharField(required=True)
        info = forms.CharField(required=True, widget=forms.Textarea)
        image = forms.ImageField(required=True)
        user = forms.CharField(required=False, widget=forms.HiddenInput)

class SpeedModelUpdateForm(forms.Form):
        title = forms.CharField(required=True)
        info = forms.CharField(required=True, widget=forms.Textarea)
        image = forms.ImageField(required=False)


class UserSignUp(forms.Form):
        username = forms.CharField(required=True)
        password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserLogIn(forms.Form):
        username = forms.CharField(required=True)
        password = forms.CharField(required=True, widget=forms.PasswordInput())