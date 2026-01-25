from django.urls import path

from .import views

urlpatterns = [
    path('<int:category_id>/', views.category_blogs, name='posts_by_category'),
]