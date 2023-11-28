from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_checkout, name='view_checkout'),
    path('add/<item_id>/', views.add_to_checkout, name='add_to_checkout'),
    path('adjust/<item_id>/', views.adjust_checkout, name='adjust_checkout'),
    path('remove/<item_id>/', views.remove_from_checkout, name='remove_from_checkout'),
]
