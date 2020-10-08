from .views import index, detailPage, update, create
from django.urls import path

urlpatterns = [
    path('', index, name='staffList'),
    path('create/', create, name='createPage'),
    path('<int:staff_id>/', detailPage, name='detailPage'),
    path('<int:staff_id>/edit', update, name='staffUpdate')
]