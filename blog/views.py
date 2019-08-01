from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客'
    }
    )

