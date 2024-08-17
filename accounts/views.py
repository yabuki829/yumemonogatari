from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import SignUpForm,activate_user
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from django.shortcuts import render
User = get_user_model()
subject = "登録完了"
message_template = """
夢物語のアカウント登録が完了しました
"""



class LoginView(AuthLoginView):
    template_name = 'accounts/login.html'  
    redirect_authenticated_user = True  
    success_url = reverse_lazy('mypage') 
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('mypage')

    def get_success_url(self):
        return self.success_url



class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
           
            return redirect('mypage')
        
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        print("フォームが有効です: ", form.cleaned_data)
        response = super().form_valid(form)
        return HttpResponse("登録確認のメールを送信しました。メールを確認してください。")

class ActivateView(TemplateView):
    template_name = 'accounts/activate.html'

    def get(self, request, uidb64, token, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if activate_user(uidb64, token):
            context['message'] = "アカウントが有効化されました。ログインしてください。"
        else:
            context['message'] = "アクティベーションリンクが無効です。"

        return self.render_to_response(context)



class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
        
    def get(self,request):
        user = self.request.user
        return render(request, 'accounts/profile.html',{
            "user":user
        })
    

from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('mypage')

    def get_object(self):
        return self.request.user