from django.shortcuts import render, redirect
from clickup_priorities import priorities
from .models import Priorities
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    date = datetime.today().strftime('%Y-%m-%d')
    try:

        priority_today = Priorities.objects.get(date=date)
        priority = Priorities.objects.exclude(date=date)

        return render(request, 'index.html',{'priorities_today': priority_today, 'priorities': priority})
        
    except:
        view_urls = ['dvd8-11485', 'dvd8-11525','dvd8-11545' ,'dvd8-11565']
        i = priorities(view_urls, {"Authorization": 'pk_49588273_8NHVFF6AVGYL1SW3OH9K6WWDFUGMK4H7' })
        x = Priorities(date=date, urgent_count=i.get('urgent_count'), urgent_time=i.get('urgent_time'), high_count=i.get('high_count'), high_time=i.get('high_time'), normal_count=i.get('normal_count'), normal_time=i.get('normal_time'), low_count=i.get('low_count'), low_time=i.get('low_time'))

        x.save()
        priority = Priorities.objects.get(date=date)
        return render(request, 'index.html',{'priorities_today': priority_today, 'priorities': priority})


def singup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', { 'form': UserCreationForm})
    else: 
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'user already exist'
                })
            except ValueError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Put valid values'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'password do not match'
        })


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or Password is incorrect'
            })
        else:
            login(request, user)
            return redirect('index')

@login_required
def signout(request):
    logout(request)
    return redirect('signin')
