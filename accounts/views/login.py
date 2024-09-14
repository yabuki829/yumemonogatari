from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from utils.debug import DeBug

User = get_user_model()

class LoginView(AuthLoginView):
    template_name = 'accounts/login.html'  
    redirect_authenticated_user = True  
    success_url = reverse_lazy('mypage') 

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        DeBug.pprint("テスト")
        return self.success_url