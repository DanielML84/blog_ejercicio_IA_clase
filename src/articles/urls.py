from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-mi/', views.about, name='about'),
    path('articulos/<slug:slug>/', views.detail, name='detail'),
]