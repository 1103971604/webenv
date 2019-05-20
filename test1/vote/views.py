from django.shortcuts import render
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):
    user=request.COOKIES.get('username')
    if request.COOKIES.get('username'):
        listA=list.objects.all()
        return render(request,'vote/index.html',locals())
    else:
        return render(request,'vote/login.html')

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
    if request.method == 'GET':
        return render(request,'vote/login.html')
    elif request.method == 'POST':
        a=request.POST['go']
        if a =='注册':
            user = UserInfo.objects.filter(username=request.POST['username'], pwd=request.POST['pwd'])
            if request.POST['username'] != '' and request.POST['pwd']!='':
                newuser=UserInfo()
                newuser.username=request.POST['username']
                newuser.pwd=request.POST['pwd']
                newuser.save()
                tip='注册成功请登录'
                return render(request,'vote/login.html',locals())
            else:
                tip='用户名存在'
                return render(request,'vote/login.html',locals())
        else:
            user=UserInfo.objects.filter(username=request.POST['username'],pwd=request.POST['pwd'])
            if user:
                listA = list.objects.all()
                res=render(request,'vote/index.html',locals())
                res.set_cookie('username',request.POST['username'])
                user = request.COOKIES.get('username')
                return res
            else:
                return HttpResponse('登录失败')

def loginout(request):
    res=render(request,'vote/login.html')
    res.delete_cookie('username')
    # HttpResponse().delete_cookie('username')
    # return render(request,'vote/login.html')
    return res









