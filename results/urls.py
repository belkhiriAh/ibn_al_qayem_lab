from django.urls import path
from . import views

urlpatterns = [
    path('verify/<str:result_number>/', views.verify_result, name='verify_result'),
    path('manage/', views.manage_results, name='manage_results'),
    path('add/', views.add_result, name='add_result'),
    path('edit/<str:result_number>/', views.edit_result, name='edit_result'),
    path('delete/<str:result_number>/', views.delete_result, name='delete_result'),
]
