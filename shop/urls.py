from django.urls import path
from .views import ProductDetailView, ProductListView
from .views import SignUpView, SignInView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout")
]


