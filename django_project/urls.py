
from django.contrib import admin
from django.conf import settings #chatgpt
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static #chatgpt


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("articles/", include("articles.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")), #chatgpt
    #path("ckeditor/", include("ckeditor.urls")),
    path("", include("pages.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)