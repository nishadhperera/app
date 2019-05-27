from django.urls import path, re_path

from . import views

app_name = 'articles'

urlpatterns = [
    # /articles/
    path('', views.index, name='welcome'),
    # /articles/list
    path('list/', views.list_articles, name='list_articles'),
    # /articles/article-id
    re_path(r'^(?:article-(?P<id>\d+)/)?$',
            views.view_article,
            name='view_article'),
    # /articles/id
    path('<int:id>/', views.view_article, name='view_article'),
    # /articles/add
    path('add/', views.add_article, name='add_article'),
]
