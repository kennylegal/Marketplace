from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from services.service_factory import service_container
from services.dto.Userdto import UserCreateDto
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from services.decorator import unauthorized_user, allowed_users
from django.contrib import messages


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def list(request):
    user = service_container.user_services().listUsers()
    context = {
        'user': user
    }
    return render(request, 'marketplace/User/index.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def userDetail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        'user': user
    }
    return render(request, 'marketplace/User/details.html', context)


def __inputs(user, request):
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.username = request.POST['username']
    user.password = request.POST['password']
    user.email = request.POST['email']
    return user


def __save_if_request(request: HttpRequest) -> UserCreateDto:
    userDto = UserCreateDto()
    __inputs(userDto, request)
    return userDto


def __save_if_post_method(context, request):
    if request.method == 'POST':
        try:
            user = __save_if_request(request)
            service_container.user_services().create(user)
            context['saved'] = True
        except Exception as e:
            print(e)
            context['saved'] = False


@unauthorized_user
def create(request):
    context = {}
    __save_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("user_index")
    return render(request, "marketplace/User/Register.html", context)


@unauthorized_user
def loginPage(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('userPage')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {
        }
        return render(request, 'marketplace/User/Login.html', context)


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('indexPage')


# def clean_email(email, context):
#     mail = User.objects.filter(email__iexact=email)
#     if mail.exists():
#         context['message'] = 'Email Already exist'
#         print(context)
#     return email