from django.views.generic import TemplateView
from ..forms import activate_user
from django.shortcuts import redirect

class ActivateView(TemplateView):
    template_name = 'accounts/activate.html'

    def get(self, request, uidb64, token, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if activate_user(uidb64, token):
            context['message'] = "アカウントが有効化されました。ログインしてください。"
        else:
            context['message'] = "アクティベーションリンクが無効です。"

        return self.render_to_response(context)
