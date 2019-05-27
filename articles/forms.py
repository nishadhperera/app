from django import forms


class AddArticleForm(forms.Form):
    author_name = forms.CharField(label='Author', max_length=30)
    article_title = forms.CharField(label='Title', max_length=50)
    article_subject = forms.CharField(label='Subject', max_length=75)
    article_body = forms.CharField(label='Body', max_length=100)
