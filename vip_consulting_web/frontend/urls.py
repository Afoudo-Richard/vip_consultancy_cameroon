from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ),
    path('about/', views.about),
    path('login/', views.login),
    path('book-consultation/', views.book_consultation)
]
