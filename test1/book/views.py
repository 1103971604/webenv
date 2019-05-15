from django.shortcuts import render
from django.http import HttpResponse
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