from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from base.forms import RoomForm
from base.models import Room, Topic


def home(request):
    q = request.GET.get("q", "")
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    return render(
        request,
        "base/home.html",
        {"rooms": rooms, "room_count": room_count, "topics": topics},
    )


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
