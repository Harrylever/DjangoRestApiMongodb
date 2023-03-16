"""
Tutorials url config
"""
from django.urls import path
from . import views

urlpatterns = [
    path('tutorials/', views.tutorial_list),
    path('tutorials/<int:id>', views.tutorial_detail)
]
