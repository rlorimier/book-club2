from django.contrib import admin
from django.urls import path, include
from .views import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog-urls'),
    path('accounts/', include('allauth.urls')),
]

handler404 = 'club2.views.handler404'
