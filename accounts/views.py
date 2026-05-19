from django.urls import reverse_lazy
from django.views import generic , View
from .forms import RegisterForm , LoginForm
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

# Create your views here.

class SignupView(generic.CreateView):
    template_name = "signup.html"
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:login")

class LoginView(View):
    template_name = "login.html"
    
    def get(self,request):
        form = LoginForm()
        return render (request,self.template_name,{"form":form})
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request,email=email,password=password)
            if not user:
                messages.error(request,"Invalid Email or Password")
                return redirect ("accounts:login")
            login(request,user)
            return redirect ("tasks:home")
        return render (request,self.template_name,{"form":form})
    
    
class LogoutView(View):
    
    def post(self,request):
        logout(request)
        return redirect ("accounts:login")