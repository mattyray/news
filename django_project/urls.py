from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Includes accounts-related URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth URLs (login, logout, etc.)
    path('articles/', include('articles.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # CKEditor-related URLs
    path('', include('pages.urls')),  # Home or landing page
    path('tutorials/', include('tutorials.urls')),  # Tutorials URLs
    path('quizzes/', include('quizzes.urls')),  # Quizzes URLs
]

# Serve static and media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
