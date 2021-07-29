from cwash.models import Booking, Profile, Washplan, services
from django.contrib.auth.models import User
from cwash.forms import AppointmentForm, SignUpForm, UpdateProfileForm, UpdateUserForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.


def index(request):
    plans = Washplan.objects.all().order_by('price')
    service = services.objects.all()

    return render(request, 'index.html', {'plans': plans, 'service': service})


def signup(request):
    print('here')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    bookings = Booking.objects.filter(user=current_user.id).all

    return render(request, 'registration/profile.html', {"bookings": bookings})


@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    obj = get_object_or_404(Profile, user_id=id)
    obj2 = get_object_or_404(User, id=id)
    form = UpdateProfileForm(request.POST or None, request.FILES, instance=obj)
    form2 = UpdateUserForm(request.POST or None, instance=obj2)
    if form.is_valid() and form2.is_valid():
        form.save()
        form2.save()
        return HttpResponseRedirect("/profile")

    bookings = Booking.objects.all()

    return render(request, "registration/update_profile.html", {"form": form, "form2": form2})


@login_required(login_url='/accounts/login/')
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.email = request.user.email
            user = form.save()
            user.save()
        return redirect('book')
    else:
        form = AppointmentForm()
    return render(request, 'book.html', {'form': form})

def about(request):
   
    return render(request, 'about.html')
