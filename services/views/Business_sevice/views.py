from services.service_factory import service_container
from services.dto.business_dto import BusinessUpdateDto
from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from services.models import BusinessOwner
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url='login')
def index(request):
    owner = service_container.business_owner_service().list()

    context = {'owner': owner}
    return render(request, 'marketplace/Business Owner/index.html', context)


@login_required(login_url='login')
def detailPage(request, business_id):
    try:
        owner = service_container.business_owner_service().details(business_id)
    except BusinessOwner.DoesNotExist:
        raise Http404
    context = {
        'owner': owner
    }
    return render(request, 'marketplace/Business Owner/details.html', context)

