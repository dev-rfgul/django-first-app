
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.jinja,name='jinja'),
]
