from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django import forms
from .models import Post
from  django.contrib.auth.models import User 
class SignupForm(UserCreationForm):
    class Meta:
        model=User 
        fields=['username','first_name','last_name','email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'password1':forms.TextInput(attrs={'class':'form-control'}),
                 'password2':forms.TextInput(attrs={'class':'form-control'}),
        }
class LoginForm(AuthenticationForm):
    class Meta:
        model=User 
        fields=['username','first_name','last_name','email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'password1':forms.TextInput(attrs={'class':'form-control'}),
                 'password2':forms.TextInput(attrs={'class':'form-control'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','desc']
        labels={'title':'Title','desc':'Description'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'desc':forms.Textarea(attrs={'class':'form-control'}),}