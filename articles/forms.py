from django import forms
from .models import Article, Comment
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ('title', 'body')
