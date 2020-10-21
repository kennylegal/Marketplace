from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from services.dto.customer_dto import CustomerUpdate
from .dto.business_dto import BusinessUpdateDto
from .service_factory import service_container
from .models import BusinessOwner, Customer, MailList, Comment

# Create your views here.


@login_required(login_url='login')
def userPage(request):
    customer_name = request.user.customer.name
    id = request.user.businessowner.id
    details = service_container.customer_management_service().details(customer_name)
    context = {
        'details': details,
        'business': id,
    }
    return render(request, 'marketplace/Profile/Single.html', context)


@login_required(login_url='login')
def businessProfile(request):
    business_id = request.user.businessowner.id
    owners_comment = Comment.objects.filter(to=business_id)
    name = request.user.customer.name
    business = service_container.business_owner_service().details(business_id)
    context = {
        "business": business,
        "name": name,
        'business_id': business_id,
        'comment':owners_comment
    }
    return render(request, 'marketplace/Profile/Single2.html', context)


def __inputs(owners, request):
    owners.phone_no = request.POST['phone_no']
    owners.company_name = request.POST['company_name']
    owners.company_address = request.POST['company_address']
    owners.service_title = request.POST['service_title']
    owners.service_description = request.POST['service_description']
    owners.CAC_code = request.POST['CAC_code']
    owners.guarantors_name = request.POST['guarantors_name']
    owners.guarantors_phone_no = request.POST['guarantors_phone_no']
    owners.guarantors_address = request.POST['guarantors_address']
    return owners


def __update_progress(business_id, request: HttpRequest) -> BusinessUpdateDto:
    businessDto = BusinessUpdateDto()
    businessDto.id = business_id
    __inputs(businessDto, request)
    return businessDto


def __update_if_post_method(context, business_id: int, request):
    if request.method == 'POST':
        try:
            owner = __update_progress(business_id, request)
            service_container.business_owner_service().update(business_id, owner)
            context['saved'] = True
        except Exception as error:
            print(error)
            context['saved'] = False


@login_required(login_url='login')
def update(request, business_id):
    business_id = request.user.businessowner.id
    owner = BusinessOwner.objects.get(id=business_id)
    context = {
        'owner': owner,
        'business_id': business_id
    }
    __update_if_post_method(context, business_id, request)
    if request.method == 'POST' and context['saved']:
        return redirect('BusinessProfile')
    return render(request, 'marketplace/Business Owner/update.html', context)




def __input(customer, request):
    customer.name = request.POST['name']
    customer.phone_no = request.POST['phone_no']
    customer.home_address = request.POST['home_address']
    customer.DOB = request.POST['DOB']
    customer.social_media = request.POST['social_media']
    return customer


def __customer_inputs(customer_name: str, request: HttpRequest) -> CustomerUpdate:
    customerDto = CustomerUpdate()
    customerDto.name = customer_name
    __input(customerDto, request)
    return customerDto


def __update_if_method_is_post(context, customer_name, request):
    if request.method == 'POST':
        try:
            customer = __customer_inputs(customer_name, request)
            service_container.customer_management_service().update(customer_name, customer)
            context['saved'] = True
        except Exception as error:
            print(error)
            context['saved'] = False


@login_required(login_url='login')
def update_customer(request, customer_name):
    customer_name = request.user.customer.name
    customer = get_object_or_404(Customer, name=customer_name)
    context = {
        'customer': customer,
        'customer_name': customer_name
    }
    __update_if_method_is_post(context, customer_name, request)
    if request.method == 'POST' and context['saved']:
        return redirect('userPage')
    return render(request, 'marketplace/Customer/updates.html', context)


def __search(query):
    queryset = BusinessOwner.objects.filter(service_title__icontains=query)
    return queryset


def search(request):
    query = request.GET['query']
    result = __search(query)
    context = {
        'result': result
    }
    return render(request, 'marketplace/search.html', context)


def __mailinput(mail, context, request):
    if request.method == 'POST':
        MailList.objects.create(email=mail)
        context['saved'] = True
    else:
        context['saved'] = False


def mailview(request):
    mail = request.POST['email']
    context = {}
    __mailinput(mail, context, request)
    if request.method == 'POST' and context['saved']:
        return redirect('indexPage')
    return render(request, 'marketplace/Profile/index.html', context)


@login_required(login_url='login')
def commentcreate(request, business_id):
    owner = get_object_or_404(BusinessOwner, id=business_id)
    user = request.user.username
    form = CommentForm(request.POST or None)
    if owner is not None:
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comments = form.cleaned_data.get('comment')
            Comment.objects.create(to=owner, name=user, comment=comments)
            return redirect('userPage')
        else:
            print('form not valid')
    else:
        print('Customer does not exist')
    context = {
        'form': form,
        'owner' : owner,
        'business' : business_id
    }
    return render(request, 'marketplace/comments/create.html', context)
