"""
URL configuration for studybud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.urls import path, include
from django.shortcuts import render, HttpResponse, redirect

def profile(request, id):
    acc = User.objects.get(id = id)
    return render(request, 'profile.html', {'acc':acc})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
            return redirect('/login')
        
        user = authenticate(request, username=username, password= password)
        
        if user:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('/')
        else:
            messages.error(request, "Wrong password")
            return redirect('/login')
        return redirect('/')
    
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('/')
    

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('profile/<int:id>/', profile, name='profile'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage),
]
