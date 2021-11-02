from django.contrib.auth import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from .models import Business, User, NeighbourHood
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field


class BusinessForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'BUSINESS'
    helper.add_input(Submit('post', 'post',css_class = 'btn btn-warning'))

    class Meta:
        model = Business
        fields = [
            'name',
            'image',
            'email'
        ]


class NeighbourhoodForm(forms.ModelForm):

    class Meta:
        model = NeighbourHood
        fields = [
            'name',
            'location',
            'occupants_count'
        ]
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image',
                'location']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

