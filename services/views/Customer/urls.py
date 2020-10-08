from django.urls import path
from.views import index, detailPage

urlpatterns = [
    path('', index, name='customer_index'),
    path('<str:customer_name>/', detailPage, name='customer_details'),
]