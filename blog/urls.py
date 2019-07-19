from django.urls import path
from . import views

urlpatterns = [
    path('', views.a_view, name='a_view'),
]
