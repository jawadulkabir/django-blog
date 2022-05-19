from . import views
from django.urls import path

urlpatterns = [
    path('', views.register, name='users-register'),
    #path('about/', views.about, name='blog-about'),
]