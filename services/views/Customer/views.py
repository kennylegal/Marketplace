from services.service_factory import service_container
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from services.decorator import staff_only


@login_required(login_url='login')
def index(request):
    customer = service_container.customer_management_service().list()
    context = {'customer': customer}
    return render(request, 'marketplace/Customer/index.html', context)


@login_required(login_url='login')
def detailPage(request, customer_name):
    customer = service_container.customer_management_service().details(customer_name)
    context = {
      'customer': customer,
    }
    return render(request, 'marketplace/Customer/details.html', context)

