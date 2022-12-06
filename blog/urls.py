from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('new/', views.new_post, name='new_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
]
