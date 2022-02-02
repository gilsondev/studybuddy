from django.shortcuts import get_object_or_404, redirect, render

from base.forms import RoomForm
from base.models import Room


def home(request):
    rooms = Room.objects.all()
    return render(request, "base/home.html", {"rooms": rooms})


def room(request, pk):
    room = Room.objects.get(pk=pk)
    return render(request, "base/room.html", {"room": room})


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")

    return render(request, "base/room_form.html", {"form": form})


def update_room(request, pk):
    room = get_object_or_404(Room, id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect("home")

    return render(request, "base/room_form.html", {"form": form})


def delete_room(request, pk):
    room = get_object_or_404(Room, id=pk)

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": room})
