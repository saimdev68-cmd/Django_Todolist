from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email","username","password1","password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""
        self.fields["username"].widget.attrs["placeholder"] = "Enter Username..."
        self.fields["email"].widget.attrs["placeholder"] = "Enter Email..."
        self.fields["password1"].widget.attrs["placeholder"] = "Enter Password..."
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password..."

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder":"Enter Email..."
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Enter Password..."
    }))
    