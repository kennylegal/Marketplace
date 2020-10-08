from django.shortcuts import render
from services.decorator import unauthorized_user


@unauthorized_user
def index(request):
    return render(request, 'marketplace/Profile/index.html')