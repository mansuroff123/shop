from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.views.generic import CreateView

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'
    context_object_name = 'products'
    paginate_by = 1


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
class SignInView(LoginView):
    form_class = SignInForm
    template_name = "registration/sign_in.html"
