from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Item

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2','check')
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'your username',
        'class':'form-control',
        }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'your email',
        'class':'form-control',
        }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'enter password',
        'class':'form-control',
        }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'confirm password',
        'class':'form-control',
        }))
    check=forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'id':'chk',
        'onclick':'func()',
        'class':'form-check-input',
        }))
        
html_class='form-control'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('first_name','last_name','address','city','state','email','zipcode',)
        widgets={
           'first_name':forms.TextInput(attrs={
              'class':html_class}),
           'last_name':forms.TextInput(attrs={
              'class':html_class}),
           'address':forms.TextInput(attrs={
              'class':html_class}),
           'city':forms.TextInput(attrs={
              'class':html_class}),
           'state':forms.TextInput(attrs={
              'class':html_class,}),
           'email':forms.TextInput(attrs={
              'class':html_class,}),
           'zipcode':forms.TextInput(attrs={
              'class':html_class,}),
           
        }