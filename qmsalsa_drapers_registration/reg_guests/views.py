from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'reg_guests/guest_list.html', {})
    # return HttpResponse("Hello, world. You're at the reg_guests index.")