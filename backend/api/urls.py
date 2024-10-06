from django.urls import path
from .views import PredictionView

urlpatterns=[
    path('api/stats', PredictionView.as_view(), name = 'stats')
]