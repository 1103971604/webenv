from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.generic.base import View
# Create your views here.
from django.contrib.auth import authenticate,login ,logout


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
        user = authenticate(request, username=username, password=pwd)
        print(user)
        if user:
            login(request, user)
            listA = list.objects.all()
            return render(request,'vote/index.html',locals())
        else:
            return render(request, 'vote/login.html', {"error": "用户名或者密码错误"})

def Register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        user = authenticate(request, username=username, password=pwd)
        if user:
            error = "用户存在"
            return render(request, 'vote/login.html',locals())
        else:
            Myuser.objects.create_user(username=username, password=pwd, url='http://zzy0371.com')
            return redirect(reverse('votetest:login'))




def loginout(request):
    res=render(request,'vote/login.html')
    res.delete_cookie('username')
    request.session.flush()
    # HttpResponse().delete_cookie('username')
    # return render(request,'vote/login.html')
    return res









