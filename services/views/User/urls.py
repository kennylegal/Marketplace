from django.urls import path
from services.views.User import views

urlpatterns = [
    path('', views.list, name='user_index'),
    path('create', views.create, name='create_user'),
    path('login', views.loginPage, name='login'),
    path('<int:user_id>/', views.userDetail, name='user_details'),
    path('logout/', views.logoutUser, name='logout')
    ]
