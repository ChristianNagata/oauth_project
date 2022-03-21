from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from oauth_project.settings import LOGOUT_REDIRECT_URL


@login_required
def dashboard(request):

    articles = Article.objects.all()

    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            return redirect('dashboard')

    context = {'form': form, 'articles': articles}

    return render(request, 'dashboard.html', context)


@login_required
def my_articles(request):
    articles = Article.objects.filter(author=request.user)
    context = {'articles': articles}
    return render(request, 'my_articles.html', context)
