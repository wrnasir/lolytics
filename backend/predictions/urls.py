from django.urls import path
from . import views

urlpatterns=[
    path('', views.run_player_linear_regression)
]