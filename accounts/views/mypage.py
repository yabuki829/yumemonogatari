from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.shortcuts import render


class MyPageView(TemplateView):
    template_name = 'accounts/mypage.html'
    def dispatch(self, request, *args, **kwargs):
        # ログインしてなかったらログイン画面にリダイレクト
        if self.request.user.is_authenticated == False:
            return redirect('login')
        
        return super().dispatch(request, *args, **kwargs)
        
        
    def get(self,request):
        user = self.request.user
        return render(request, 'accounts/mypage.html',{
            "user":user
        })
    
