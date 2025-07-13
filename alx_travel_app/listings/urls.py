from django.urls import path
from . import views

urlpatterns = [
    # Placeholder route to avoid error
    path('', views.placeholder, name='placeholder'),
]

