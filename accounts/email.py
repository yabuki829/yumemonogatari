from django.conf import settings
from templated_mail.mail import BaseEmailMessage

class EmailManager(BaseEmailMessage):
    def send(self, to, *args, **kwags):
        self.render()
        self.to = to
        self.cc = kwags.pop("cc", [])
        self.bcc = kwags.pop("bcc", [])
        self.reply_to = kwags.pop("reply_to", [])
        self.from_email = kwags.pop(
            "from_email", f"{settings.SITE_NAME} <{settings.DEFAULT_FROM_EMAIL}>"
        )
        super(BaseEmailMessage, self).send(*args, **kwags)