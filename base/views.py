from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import forms
from .models import Room, Topic

# Create your views here.


def home(request):
    query = request.GET.get('q')
    topics = Topic.objects.all()

    if query:
        rooms = Room.objects.filter(topic__name__icontains = query)
        return render(request, 'base/home.html', context={'rooms': rooms, 'topics': topics, 'query':query})
    else:
        rooms = Room.objects.all()
    return render(request, 'base/home.html', context={'rooms': rooms, 'topics': topics})

def room(request, id):
    room = Room.objects.get(id = id)
    return render(request, 'base/room.html', {'room': room})

@login_required(login_url='login')
def createRoom(request):
    form = forms.RoomForm()

    if request.method == 'POST':
        # print(request.POST)
        room = forms.RoomForm(request.POST)
        if room.is_valid():
            room.save()

        return redirect('/')

            

    return render(request, 'base/room_form.html', {'form':form})

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = forms.RoomForm(instance=room)

    if request.method == 'POST':
        # print(request.POST)
        
        updated_room = forms.RoomForm(request.POST, instance=room)
        if updated_room.is_valid():
            updated_room.save()

        return redirect('/')
    return render(request, 'base/room_form.html', {'form':form, 'room':room})

def deleteRoom(request, pk):
    room = get_object_or_404(Room, id=pk)
    room.delete()

    

    messages.success(request, "Item deleted successfully.")

    return redirect('home')