from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

from . import forms
from .models import Room

# Create your views here.

rooms = [
    {'id':1, 'name': 'Python learning'},
    {'id':2, 'name': 'Django room'},
    {'id':3, 'name': 'Assembly learning'},
]


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', context={'rooms': rooms})

def room(request, id):
    room = Room.objects.get(id = id)
    return render(request, 'base/room.html', {'room': room})


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