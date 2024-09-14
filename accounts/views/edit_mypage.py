from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import MyPageForm

from django.contrib.auth import get_user_model
User = get_user_model()


class EditMypageView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = MyPageForm
    template_name = 'accounts/edit_mypage.html'
    success_url = reverse_lazy('mypage')

    def get_object(self):
        return self.request.user