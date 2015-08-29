# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from accounts.models import UserProfile
from django.forms.extras.widgets import SelectDateWidget

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','password1', 'password2', "email",)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'register'
        self.helper.form_method = 'post'
        self.helper.form_action = 'user:register'
        self.helper.add_input(Submit('submit', 'Register'))

    def save(self,commit = True):   
        user = super(RegistrationForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active=True
        if commit:
            user.save()
        return user    

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            #check password match
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. "+
                    "Please enter both fields again.")
        return self.cleaned_data

    def clean_email(self):        
        if User.objects.filter(email__iexact=self.cleaned_data['email']).count():
            raise forms.ValidationError(u'This email address is already in use. '+
                'Please supply a different email address.')
        return self.cleaned_data['email']

class LoginForm(forms.Form):
    username=forms.CharField(label='Your username or email',
        widget=forms.widgets.TextInput(), required=True)
    password=forms.CharField(label='Password', widget=forms.widgets.PasswordInput(),
        required=True)
    class Meta:
        fields=['username','password']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'login'
        self.helper.form_method = 'post'
        self.helper.form_action = 'user:login'
        self.helper.add_input(Submit('submit', 'Login')) 

class UserProfileForm(forms.ModelForm):
    birthday=forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    class Meta:
        model = UserProfile
        exclude=('user','rank','follows','followers_count','follows_count','follow_tags')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'editprofile'
        self.helper.form_method = 'post'
        self.helper.form_action = 'user:edit_profile'
        self.helper.add_input(Submit('submit', 'Update'))  