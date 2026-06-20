from django.urls import path
from .views import *

urlpatterns = [
    path('', expense_list, name='expense_list'),
    path('add/', add_expense, name='add_expense'),
    path('delete/<int:id>/', delete_expense, name='delete_expense'),
]