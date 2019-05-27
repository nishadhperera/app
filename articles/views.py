from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddArticleForm

from .models import Article


def index(request):
    return render(request, 'articles/welcome.html')


def view_article(request, id):
    article = Article.objects.get(id=id)
    return HttpResponse(
        '<h2> ' + article.article_title + ' </h2>'
        '<h3> by ' + article.author + ' on ' + article.subject + '</h3>'
        '<body>' + article.body + '</body>'
    )


def list_articles(request):
    all_articles = Article.objects.all()
    context = {
        'all_articles': all_articles
    }
    return render(request, 'articles/article_list.html', context)


def add_article(request):
    if request.method == 'POST':
        form = AddArticleForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data['author_name']
            title = form.cleaned_data['article_title']
            subject = form.cleaned_data['article_subject']
            body = form.cleaned_data['article_body']
            new_article = Article(
                author=author,
                article_title=title,
                subject=subject,
                body=body
            )
            new_article.save()
            return redirect('articles:list_articles')
    else:
        form = AddArticleForm()
    return render(request, 'articles/add_article.html', {'form': form})
