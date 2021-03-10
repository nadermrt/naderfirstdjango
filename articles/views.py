from django.shortcuts import render,HttpResponse
from . import models
# Create your views here.

def articles_list(request):
    articles = models.Article.objects.all().order_by('date')
    
    args = {'firstarticles':articles}
    return render(request, 'articles/articleslist.html', args )

def articles_detail(request , article_details):
    # return HttpResponse(article_details)
    article = models.Article.objects.get(slug=article_details)
    return render(request , 'articles/article_Details.html',{'articless':article})