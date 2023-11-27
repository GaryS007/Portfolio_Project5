from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_checkout, name='view_checkout'),
    path('add/<item_id>/', views.add_to_checkout, name='add_to_checkout'),
]
