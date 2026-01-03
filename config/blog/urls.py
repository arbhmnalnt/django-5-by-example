from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('edit/<slug:slug>', views.post_edit, name='post_edit'),
    path('create/', views.post_create, name='post_create'),
    path('post/<path:slug>', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
    
]