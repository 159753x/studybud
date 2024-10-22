from django.urls import path
from .views import home, room, createRoom, updateRoom

urlpatterns = [
    path('', home),
    path('room/<int:id>/', room),
    path('create-room/', createRoom),
    path('update-room/<int:pk>', updateRoom)
]