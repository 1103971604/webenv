from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.generic.base import View
# Create your views here.
from django.contrib.auth import authenticate,login ,logout
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings

# 绘图 模块
from PIL import Image,ImageDraw,ImageFont
import io,random

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
        verifycode=request.POST.get('verifycode')

        if verifycode==request.session.get('verifycode'):
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
        else:
            return render(request, 'vote/login.html', {"error": "验证码错误"})

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


def verifycode(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))

    width=100
    heigth=50
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('LHANDW.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0],fontcolor=fontcolor,font=font)
    draw.text((25, 2), rand_str[1],fontcolor=fontcolor,font=font)
    draw.text((50, 2), rand_str[2],fontcolor=fontcolor,font=font)
    draw.text((75, 2), rand_str[3],fontcolor=fontcolor,font=font)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')







