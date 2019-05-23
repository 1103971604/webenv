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
    article.Readnum += 1
    article.save()
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

        print(article.bodytxt)

        return render(request,'single.html',locals())


        # return redirect(reverse('app1:single'))