from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import SignUpForm,activate_user
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()
subject = "登録完了"
message_template = """
夢物語のアカウント登録が完了しました
"""

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

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


