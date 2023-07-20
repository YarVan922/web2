from django.urls import path
from .views import index, lesson_4

urlpatterns = [
    path('',index),
    path('top-sellers/', top_sellers),
]
