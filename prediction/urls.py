from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.prediction_form, name='prediction_form'),
    path('result/<int:prediction_id>/', views.prediction_result, name='prediction_result'),
]
