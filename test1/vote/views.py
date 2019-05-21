from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.generic.base import View
# Create your views here.


def func1(func):
    def a(request,*args):
        un=request.session.get('username')
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


@func1
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

@func1
def listcountA(request,titleid):
    tit=list.objects.get(pk=titleid)
    return render(request, 'vote/count.html',{'tit':tit})


def Login(request):


    # 50------63行 自定义模型 方法
# -----------------------------------------------------------------------------------------
    if request.method == 'GET':
        return render(request,'vote/login.html')
    elif request.method == 'POST':
        user = UserInfo.objects.filter(username=request.POST['username'], pwd=request.POST['pwd'])
        print(user)
        if user:
            listA = list.objects.all()
            request.session['username'] = request.POST['username']
            username=request.session.get('username')
            return render(request, 'vote/index.html', locals())
        else:
            return render(request,'vote/login.html',{'error':'cuowu'})
# ------------------------------------------------------------------------------------------


def Register(request):
    pass
    # 68-86 行自己写的模型 注册
 # -----------------------------------------------------------------------------
    # return HttpResponse('注册')
    username=request.POST.get('username')
    pwd=request.POST.get('pwd')
    user=UserInfo.objects.filter(username=username,pwd=pwd)
    if user:
        error='用户名存在'
        # return redirect(reverse('votetest:login',kwargs={'error':'用户名存在'}))
        return render(request,'vote/login.html',locals())
    else:
        newuser=UserInfo()
        newuser.username=username
        newuser.pwd=pwd
        newuser.save()
        return redirect(reverse('votetest:index'))
# -----------------------------------------------------------------------------


def loginout(request):
    res=render(request,'vote/login.html')
    res.delete_cookie('username')
    request.session.flush()
    # HttpResponse().delete_cookie('username')
    # return render(request,'vote/login.html')
    return res









