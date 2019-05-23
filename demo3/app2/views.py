from django.shortcuts import render,redirect,reverse
from .models import Comment
from app1.models import Articles
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

def Msg(request,id):

    if request.method=='POST':
        article = Articles.objects.get(pk=id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        comment = request.POST.get('comment')
        Messige = Comment()
        Messige.username = name
        Messige.email = email
        Messige.url = url
        Messige.tex = comment
        Messige.title = article
        Messige.save()
        # return HttpResponseRedirect('/app1/single/%s/'%(id,))
        return redirect(reverse('app1:single',args=(id,)))




