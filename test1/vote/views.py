from django.shortcuts import render
from .models import list,listcount
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):
    listA=list.objects.all()
    return render(request,'vote/index.html',{'list':listA})


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
