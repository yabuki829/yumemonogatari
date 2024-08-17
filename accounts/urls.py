from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
    path('profile/', views.ProfileView.as_view(), name='mypage'),
    path('profile/edit/', views.EditProfileView.as_view(), name='profile_edit'),
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)