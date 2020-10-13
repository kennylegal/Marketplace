from random import randint
from services.service_factory import service_container
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from services.decorator import admin_only, staff_only
from services.models import Staff
from django.http import Http404, HttpRequest
from services.dto.staff_dto import UpdateStaff, CreateStaff


@login_required(login_url='login')
@admin_only
def index(request):
    staff = service_container.staff_services().list()
    context = {
        'staff': staff
    }
    return render(request, 'marketplace/Staff/index.html', context)


@login_required(login_url='login')
@admin_only
def detailPage(request, staff_id):
    staff = service_container.staff_services().details(staff_id)
    context = {
        'staff': staff
    }
    return render(request, 'marketplace/Staff/details.html', context)

#
# def __inputs(staff, request):
#     staff.user = request.user
#     staff.DOB = request.POST['DOB']
#     staff.address = request.POST['address']
#     staff.job_title = request.POST['job_title']
#     return staff
#
#
# def __update_in_progress(staff_id: int, request):
#     staffDto = UpdateStaff()
#     staffDto.id = staff_id
#     __input(staffDto, request)
#     return staffDto
#
#
# def __update_if_post_method(context, staff_id, request):
#     if request.method == 'POST':
#         try:
#             staff = __update_in_progress(staff_id, request)
#             service_container.staff_services().update(staff_id, staff)
#             context['saved'] = True
#         except Exception as error:
#             print(error)
#             context['saved'] = False

#
# @login_required(login_url='login')
# @staff_only
# def update(request, staff_id):
#     staff = get_object_or_404(Staff, id=staff_id)
#     context = {
#         'staff': staff,
#         'staff_id': staff_id
#     }
#     __update_if_post_method(context, staff_id, request)
#     if request.method == 'POST' and context['saved']:
#         return redirect('staffList')
#     return render(request, 'marketplace/Staff/update.html', context)


def __input(staff, request):
    staff.user = request.user
    staff.staff_code = str(request.user) + str(randint(100, 200))
    staff.DOB = request.POST['DOB']
    staff.address = request.POST['address']
    staff.job_title = request.POST['job_title']
    return staff


def __create_in_progress(request):
    staffDto = CreateStaff()
    __input(staffDto, request)
    return staffDto


def __create_if_post_method(context, request):
    if request.method == 'POST':
        try:
            staff = __create_in_progress(request)
            if __staff_search(staff.user):
                service_container.staff_services().create(staff)
                context['saved'] = True
        except Exception as error:
            print(error)
            context['saved'] = False


@login_required(login_url='login')
@staff_only
def create(request):
    context = {}
    __create_if_post_method(context, request)
    if request.method == 'POST' and context['saved']:
        return redirect('userPage')
    return render(request, 'marketplace/Staff/create.html', context)


def __staff_search(username):
    staff = list(Staff.objects.all())
    if username in staff:
        print('Staff Record Exists')
    else:
        print('Your Record Has Been Saved')
        return username