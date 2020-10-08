from django.urls import path, include
from .views import about, contactPage


urlpatterns = [
    path('about', about, name='aboutPage'),
    path('contactUs', contactPage, name='contactPage'),
]