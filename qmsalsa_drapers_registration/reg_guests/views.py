from django.shortcuts import render
from django.utils import timezone
from .models import Guest
from .forms import GuestForm
from django.shortcuts import redirect

def guest_list(request):
    guests = Guest.objects.filter(registration_time__lte=timezone.now()).order_by('registration_time')
    return render(request, 'reg_guests/guest_list.html', {'guests': guests})

def register_new(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.save()
            return redirect('guest_list')
    else:
        form = GuestForm()
    return render(request, 'reg_guests/register_new.html', {'form': form})