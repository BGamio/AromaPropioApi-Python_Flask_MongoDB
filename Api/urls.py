from django.urls import path
from Api import views

urlpatterns = [
    path('posts/', views.post_endpoint, name='post_list'),
    path('posts/<int:id>/', views.post_endpoint, name='post_detail'),
    path('resennias/', views.resennia_endpoint, name='resennia_list'),
    path('resennias/<int:id>/', views.resennia_endpoint, name='resennia_detail'),
    path('libro_de_reclamaciones/', views.libro_de_reclamaciones_endpoint, name='libro_de_reclamaciones_list'),
    path('libro_de_reclamaciones/<int:id>/', views.libro_de_reclamaciones_endpoint, name='libro_de_reclamaciones_detail'),
]