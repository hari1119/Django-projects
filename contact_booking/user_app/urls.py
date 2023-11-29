from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView, LoginView
from .views import ValidateUser

app_name = "user"

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('validate_user/', ValidateUser.as_view(), name='validate_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]