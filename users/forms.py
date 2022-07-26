from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from PIL import Image


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [ 'first_name','last_name', 'username' , 'email', ]
            
        

class ProfileUpdateForm(forms.ModelForm):  
    class Meta:
        model = Profile
        fields = ['bio','date_of_birth','image']
        
        
