from django.urls import path
from . import views

urlpatterns = [
    path('', views.website_list, name='website_list'),
    path('create/', views.website_create, name='website_create'),
    path('<int:website_id>/delete/', views.website_delete, name='website_delete'),
    path('<int:website_id>/preview/', views.website_preview, name='website_preview'),
    path('<int:website_id>/editor/', views.edit_website_content, name='content_editor'),
    path('<int:website_id>/update/', views.save_website_content, name='website_update'),
]