from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Blog


# Create your views here.

def index(request):
    blog_list = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blog_list})


def login(request):
    blog_list = Blog.objects.all()
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    if username == '123456'  and password == '123':
       # return HttpResponse('login success!')
       response = HttpResponseRedirect('/login_ok/')
       # response.set_cookie('username', username, 3600)  # 用户名 cookie
       request.session['username']=username #将session保存到服务器
       return response
    else:
       return render(request, 'index.html', {'error': 'username or password error!', 'blogs': blog_list})


def  login_ok(request):
     blog_list = Blog.objects.all()
     # username = request.COOKIES.get('username','') # 读取浏览器 cookie
     username=request.session.get('username','') #读取用户session
     return render(request,'login_ok.html',{'user': username, 'blog_list':blog_list})


def login_out(request):
    response = HttpResponseRedirect('/index/')  # 返回首页
    # response.delete_cookie('username')  # 清理 cookie 里保存 username
    del request.session['username'] #清理用户session
    return response