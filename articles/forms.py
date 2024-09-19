from django import forms
from .models import Article, Comment

from ckeditor_uploader.widgets import CKEditorUploadingWidget #chatgpt
#from ckeditor.widgets import CKEditorUploadingWidget #chatgpt

class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget()) #chatgpt
    class Meta:
        model=Article
        fields=('title', 'body') 

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)