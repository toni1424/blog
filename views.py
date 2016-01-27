from datetime import timezone

from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article

def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def show_article(requset, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(requset, 'blog/article.html', {'article': article})