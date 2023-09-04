from django.urls import path
from . import views

app_name = 'market_app'  # App namespace

urlpatterns = [
    # List JSON data entries
    path('', views.json_data_list, name='json_data_list'),

    # Create a new JSON data entry
    path('create/', views.create_json_data, name='create_json_data'),

    # Update an existing JSON data entry
    path('update/<int:pk>/', views.update_json_data, name='update_json_data'),

    # Delete a JSON data entry
    path('delete/<int:pk>/', views.delete_json_data, name='delete_json_data'),
]
