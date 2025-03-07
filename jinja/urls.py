
from django.urls import path
from . import views

urlpatterns = [
    path('',views.jinja,name='jinja'),
]
