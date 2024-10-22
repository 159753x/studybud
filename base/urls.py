from django.urls import path
from .views import home, room, createRoom, updateRoom, deleteRoom

urlpatterns = [
    path('', home, name='home'),
    path('room/<int:id>/', room),
    path('create-room/', createRoom),
    path('update-room/<int:pk>', updateRoom),
    path('delete-room/<int:pk>', deleteRoom, name='delete-room'),
]