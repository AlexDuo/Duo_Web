# -*- coding: utf-8 -*-
# @Time : 12/18/2018 3:38 PM
# @Author : Duo Zhang
# @IDE: PyCharm
from django import forms
from register import models
class login_form(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'Please input username'}))
    password = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'Please input password'}))

    def clean(self):
        cleaned_data = self.cleaned_data

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        username_list = list(models.user_info_entity.objects.all().values_list('username'))

        