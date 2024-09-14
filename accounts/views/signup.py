from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from ..forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        # ログインしていればマイページに遷移する
        if self.request.user.is_authenticated:
            return redirect('mypage')
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        print("フォームが有効です: ", form.cleaned_data)
        response = super().form_valid(form)

        return HttpResponse("登録確認のメールを送信しました。メールを確認してください。")