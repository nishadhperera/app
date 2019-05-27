from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=30)
    article_title = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    body = models.CharField(max_length=200)
    created_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.article_title
