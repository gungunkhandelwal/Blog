from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm,EditForm


class PasswordChange(PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/password_success.html',{})


class UserRegister(generic.CreateView):
    form_class=SignUpForm
    template_name='registration/register.html'
    success_url= reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class=EditForm
    template_name='registration/edit_profile.html'
    success_url= reverse_lazy('index')

    def get_object(self):
        return self.request.user
