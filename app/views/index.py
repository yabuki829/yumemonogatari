from django.http import HttpResponse
def test(request):
    return HttpResponse("サーバーは正常に動作しています")


# views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
