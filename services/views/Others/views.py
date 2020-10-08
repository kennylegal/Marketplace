from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def about(request):

    return render(request, 'marketplace/Profile/About.html')


@login_required(login_url='login')
def contactPage(request):

    return render(request, 'marketplace/Profile/Contact.html')

