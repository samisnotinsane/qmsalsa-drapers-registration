from django.shortcuts import render
from django.utils import timezone
from .models import Guest

def guest_list(request):
    guests = Guest.objects.filter(registration_time__lte=timezone.now()).order_by('registration_time')
    return render(request, 'reg_guests/guest_list.html', {'guests': guests})
    