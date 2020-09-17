from django.urls import path
from . import views
urlpatterns =[
    path("", views.home, name = "home"),
    path("ImpactPrediction", views.ImpactPrediction, name = "ImpactPrediction"),
    path("ImpactPredictionValue", views.ImpactPredictionValue, name = "ImpactPredictionValue"),
]