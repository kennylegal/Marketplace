from .views import index, detailPage, create
from django.urls import path

urlpatterns = [
    path('list/', index, name='staffList'),
    path('', create, name='staffCreatePage'),
    path('<int:staff_id>/', detailPage, name='detailPage'),
#    path('<int:staff_id>/edit', update, name='staffUpdate')
]