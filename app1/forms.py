from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.shortcuts import render
from app1.models import Profile
'''
import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://api.github.com/users/sohommandal')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    #print("Entire JSON response")
    #print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
arr=["login","id","name","email","followers","updated_at"]
new_arr=[]
k=0
jsonResponse = response.json()
for key, value in jsonResponse.items():
    if key in arr:
        new_arr.append(value)'''

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    '''login_ID = forms.CharField(max_length = 20),
    Id  = forms.CharField(max_length = 20),
    email = forms.CharField(max_length = 20),
    followers = forms.CharField(max_length = 20),
    last_update= forms.CharField(max_length = 20),'''
    class Meta:
        model = Profile
        fields = ['username','first_name','last_name','email',]

class UserUpdateForm(UserChangeForm):
    class Meta:
            model = Profile
            fields={'email','first_name','last_name',}
