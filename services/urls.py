from django.urls import path, include
from .view import userPage, businessProfile, update_customer, update, search, mailview
from django.contrib.auth import views as auth_views


urlpatterns = [


    path('profile', userPage, name='userPage'),
    path('profile/<int:business_id>/edit', update, name='business_update'),
    path('profile/<str:customer_name>/edit', update_customer, name='update_customer'),
    path('profile/business', businessProfile, name='BusinessProfile'),

    path('search/', search, name='search'),
    path('subscribed/', mailview, name='mailview'),

    path('users/', include('services.views.User.urls')),
    path('customers/', include('services.views.Customer.urls')),
    path('business/', include('services.views.Business_sevice.urls')),
    path('', include('services.views.Others.urls')),
    path('staff/', include('services.views.Staff.urls')),

    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')

]