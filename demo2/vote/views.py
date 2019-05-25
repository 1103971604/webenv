from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.generic.base import View
# Create your views here.
from django.contrib.auth import authenticate,login ,logout
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings


def func1(func):
    def a(request,*args):
        un=request.session.get('session')
        if un :
            user = un
            return func(request,*args)
        else:
            # return render(request, 'vote/login.html')
            return redirect(reverse('votetest:login'))
    return a


@func1
def index(request):
    # un=request.COOKIES.get('username')
    listA=list.objects.all()
    return render(request,'vote/index.html',locals())



def choice(request,titleid):
    titleone = list.objects.get(pk=titleid)
    if request.method=='GET':
        return render(request,'vote/choice.html',{'title':titleone})
    elif request.method=='POST':
        value=request.POST['choice']
        listobj=listcount.objects.get(choice=value)
        listobj.num+=1
        listobj.save()
        return HttpResponseRedirect('/vote/listcountA/%s/'%(titleone.id,))


def listcountA(request,titleid):
    tit=list.objects.get(pk=titleid)
    return render(request, 'vote/count.html',{'tit':tit})


def Login(request):
    if request.method == "GET":
        return render(request, 'vote/login.html')
    else:
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        # user = authenticate(request, username=username, password=pwd)
        # 查看有没有这个用户名
        user=get_object_or_404(Myuser,username=username)
        # 判断存在的这个用户名是不是激活状态
        if user.is_active:
            # 判断这个用户名对应的密码是否一样
            if user.check_password(pwd):
                login(request, user)
                listA = list.objects.all()
                return render(request,'vote/index.html',locals())
            else:
                return render(request, 'vote/login.html', {"error": "用户名或者密码错误"})
        else:
            return render(request, 'vote/login.html', {"error": "用户未激活"})

def Register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")
        user = authenticate(request, username=username, password=pwd)
        if user:
            error = "用户存在"
            return render(request, 'vote/login.html',locals())
        else:
            user=Myuser.objects.create_user(username=username, password=pwd, url='http://zzy0371.com')
            user.is_active=False
            user.save()


            url='http://127.0.0.1:8000/vote/active/%s/'%(user.id,)
            # send_mail('激活用户1','aaaa',settings.DEFAULT_FROM_EMAIL,['1103971604@qq.com'])
            send_mail('激活',url,settings.DEFAULT_FROM_EMAIL,['1103971604@qq.com'])
            print('发送成功')



            return redirect(reverse('votetest:login'))




def loginout(request):
    res=render(request,'vote/login.html')
    res.delete_cookie('username')
    request.session.flush()
    # HttpResponse().delete_cookie('username')
    # return render(request,'vote/login.html')
    return res



def active(request,id):
    user=Myuser.objects.get(pk=id)
    user.is_active=True
    user.save()
    return render(request, 'vote/login.html', {"error": "用户激活成功"})






