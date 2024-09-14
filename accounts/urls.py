from django.urls import path
from .views import login,signup,activate,mypage,edit_mypage
urlpatterns = [
    path('login/', login.LoginView.as_view(), name='login'),
    path("signup/", signup.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', activate.ActivateView.as_view(), name='activate'),
    path('mypage/', mypage.MyPageView.as_view(), name='mypage'),
    path('edit/mypage/', edit_mypage.EditMypageView.as_view(), name='edit_mypage'),
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)