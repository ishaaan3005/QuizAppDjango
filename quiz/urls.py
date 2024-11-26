from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('quiz/', views.quiz, name='quiz'),                  # Quiz page
]
