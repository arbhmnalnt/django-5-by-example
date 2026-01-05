from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    
    path('api/posts/<path:slug>/', views.PostDetailAPIView.as_view(), name='api_post_detail'),
    path('api/posts/', views.PostListAPIView.as_view(), name='api_post_list'),
    path('edit/<slug:slug>', views.post_edit, name='post_edit'),
    path('create/', views.post_create, name='post_create'),
    path('post/<path:slug>', views.postDetailView.as_view(), name='post_detail'),
    path('', views.post_list.as_view(), name='post_list'),
    
]