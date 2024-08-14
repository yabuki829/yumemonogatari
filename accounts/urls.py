from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
]
