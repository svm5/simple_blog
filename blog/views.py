from django.shortcuts import render, redirect
from .models import Bloger, Blog

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView

from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, "index.html")


from django.views import generic


class BlogerListView(generic.ListView):
    model = Bloger


class BlogerDetailView(generic.DetailView):
    model = Bloger


class BlogsListView(generic.ListView):
    model = Blog


class BlogDetailView(generic.DetailView):
    model = Blog


# class RegisterFormView(FormView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "register.html"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Аккаунт создан")
            return redirect('/')
        else:
            form = UserCreationForm()
            return render(request, 'register.html', {"form": form})



class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'