from django.urls import path
from .views import index
urlpatterns = [
    path('', index.index, name='index'),
    path('mypage', index.index, name='mypage'),

    path('test/', index.test, name="test"),
]
