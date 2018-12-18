# -*- coding: utf-8 -*-
# @Time : 12/18/2018 2:19 PM
# @Author : Duo Zhang
# @IDE: PyCharm

from django import forms
from register import models

class register_form(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'placeholder':'Please input username'}))
    password = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'Please input password'}))
    password2 = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'Please input password again'}))
    email = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'Please input email'}))

    def clean(self):
        cleaned_data = self.cleaned_data

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        userinfo = list(models.user_info_entity.objects.all().values_list('username'))

        for i in userinfo:
            if username in i:
                raise forms.ValidationError('The user has already exist! Please try another one')
        if password2 != password:
            raise forms.ValidationError('The password are not same! Please check.')
        return cleaned_data


