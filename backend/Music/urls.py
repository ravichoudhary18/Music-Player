from django.urls import path
from Music.views import TestAPI

urlpatterns = [
    path('test/', TestAPI.as_view())
]
