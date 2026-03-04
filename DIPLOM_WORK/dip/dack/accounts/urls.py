from django.urls import path
from . import views

urlpatterns = [
    path('authan/', views.Authantication.as_view()),

]