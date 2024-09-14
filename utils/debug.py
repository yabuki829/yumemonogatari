
import logging
from django.conf import settings
class DeBug():
    def pprint(text):
        if settings.DEBUG:
            print(text)


    def loging():
        pass