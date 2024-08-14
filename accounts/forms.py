from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
User = get_user_model()

def get_activate_url(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return settings.FRONTEND_URL + "/accounts/activate/{}/{}/".format(uid, token)

subject = "登録確認"
message_template = """
夢物語をご利用ありがとうございます。
以下URLをクリックして登録を完了してください。

"""

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_active = False 
        if commit:
            user.save()
            activate_url = get_activate_url(user)
            message = message_template + activate_url
            
            # SITE_NAMEを含む差出人名を設定
            from_email = f"{settings.SITE_NAME} <{settings.DEFAULT_FROM_EMAIL}>"
            send_mail(subject, message, from_email=from_email, recipient_list=[user.email])
        return user


def activate_user(uidb64, token):    
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception:
        return False

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True
    
    return False