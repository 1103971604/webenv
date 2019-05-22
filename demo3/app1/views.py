from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Articles,Category,Pags
from django.core.paginator import Paginator
from app2.models import Comment
from django.shortcuts import render,redirect,reverse
# Create your views here.
import markdown
def index(request):

    num=request.GET.get('page')
    print(num)
    if num== None:
        num=1
    articles=Articles.objects.all().order_by('-create_time')
    paginator=Paginator(articles,1)
    page=paginator.get_page(num)
    return render(request,'index.html',{'page':page})

def single(request,id):
    article = Articles.objects.get(pk=id)
    Messiges=article.comment_set.all()
    print(Messiges)
    if request.method=='GET':
        # article.bodytxt=markdown.markdown(article.bodytxt,extensions=[
        #     "markdown.extensions.extra",
        #     "markdown.extensions.codehilite",
        #     "markdown.extensions.toc"
        # ])
        mk=markdown.Markdown(extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            "markdown.extensions.toc"
        ])
        article.bodytxt=mk.convert(article.bodytxt)
        article.toc=mk.toc

        # article.Readnum+=1
        # article.save()
        return render(request,'single.html',locals())
    else:
        name=request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        comment = request.POST.get('comment')
        Messige=Comment()
        Messige.username=name
        Messige.email=email
        Messige.url=url
        Messige.tex=comment
        Messige.title=article
        Messige.save()
        # return HttpResponseRedirect('/app1/single/%s/'%(article.id,))
        return redirect(reverse('app1:single'))