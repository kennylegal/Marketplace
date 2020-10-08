from django.urls import path
from.views import index, detailPage

urlpatterns = [
    path('', index, name='business_owner'),
    path('<int:business_id>/', detailPage, name='business_detail'),
]