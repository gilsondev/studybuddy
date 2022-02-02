from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

def home(request):
    rooms = Room.objects.all()
    return render(request, "base/home.html", {"rooms": rooms})


def room(request, pk):
    room = Room.objects.get(pk=pk)
    return render(request, "base/room.html", {"room": room})
