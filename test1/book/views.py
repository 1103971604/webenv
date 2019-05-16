from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import bookinfo,heroinfo
# Create your views here.

def index(request):
    # return HttpResponse('index')

    temp=loader.get_template('book/index.html')
    context={}
    resul=temp.render(context)
    return HttpResponse(resul)


def list(request):
    temp=loader.get_template('book/list.html')
    books=bookinfo.objects.all()
    restul=temp.render({'books':books})
    return HttpResponse(restul)

def detil(request,id):
    temp=loader.get_template('book/detil.html')
    book=bookinfo.objects.get(id=id)
    restul=temp.render({'book':book})
    return HttpResponse(restul)


def delbook(request,id):
    print(id)
    # return HttpResponse('成功')
    bookinfo.objects.get(pk=id).delete()
    return HttpResponseRedirect('/book/list/')

def deldetil(request,id):
    print(id)
    # return HttpResponse('成功')
    hero=heroinfo.objects.get(pk=id)
    a=hero.nbook.id
    hero.delete()
    return HttpResponseRedirect('/book/detil/%s/'%(a,))

def addbook(request):
    if request.method=='GET':
        return render(request,'book/addbook.html')
    elif request.method=='POST':
        bookname=request.POST['bookname']
        b1=bookinfo()
        b1.title=bookname
        b1.save()
        return HttpResponseRedirect('/book/list/')



def adddetil(request,bookid):
    if request.method=='GET':
        return render(request,'book/addhero.html', {'bookid':bookid})
    elif request.method=='POST':

        book=bookinfo.objects.get(pk=bookid)
        h1=heroinfo()
        h1.heroname=request.POST['name']
        h1.heroage = request.POST['age']
        h1.hgender = request.POST['sex']
        h1.nbook=book
        h1.save()

        return HttpResponseRedirect('/book/detil/%s/'%(bookid,))




def setbook(request,id):
    if request.method=='GET':
        return render(request,'book/setbook.html' ,{'bookid':id })
    if request.method=='POST':
        book=bookinfo.objects.get(pk=id)
        book.title=request.POST['newname']
        book.save()
        return HttpResponseRedirect('/book/list/')


def setdetil(request,id):
    if request.method=='GET':
        return render(request,'book/setdetil.html',{'heroid':id})
    elif request.method=='POST':
        h1=heroinfo.objects.get(pk=id)
        bookid=h1.nbook.id
        h1.heroname = request.POST['name']
        h1.heroage = request.POST['age']
        h1.hgender = request.POST['sex']
        h1.save()
        return HttpResponseRedirect('/book/detil/%s/' % (bookid,))





