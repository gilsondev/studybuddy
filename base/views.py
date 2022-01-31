from django.http import HttpResponse
from django.shortcuts import render


rooms = [
    {"id": 1, "name": "Lets learn python"},
    {"id": 2, "name": "Design with me"},
    {"id": 3, "name": "Frontend developer"},
]


def home(request):
    return render(request, "base/home.html", {"rooms": rooms})


def room(request, pk):
    room = next(filter(lambda item: item['id'] == pk, rooms), None)
    return render(request, "base/room.html", {"room": room})
