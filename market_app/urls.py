from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_data_table, name='stock_data_table'),
]
