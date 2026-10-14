from django.urls import path
from . import views

urlpatterns = [
    path('',views.uploadimage, name = 'uploadimage'),
]