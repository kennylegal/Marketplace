from django.http import HttpResponse
from django.shortcuts import redirect, render


def unauthorized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('userPage')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func



def staff_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'marketplace/401.html')
    return wrapper_func


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'marketplace/401.html')

    return wrapper_func

