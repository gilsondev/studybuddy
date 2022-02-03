from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.models import User

from base.forms import RoomForm
from base.models import Room, Topic


def login_page(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    has_user = User.objects.filter(username=username).exists()

    if has_user:
        user = authenticate(request, username, password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Password or user is not correct")
    else:
        messages.error(request, "User does not exist")

    return render(request, "base/login.html", {})


def register_page(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occour  during registration")

    return render(request, "base/register.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("home")


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
    room_instance = Room.objects.get(pk=pk)
    return render(request, "base/room.html", {"room": room_instance})


@login_required(login_url="login")
def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")

    return render(request, "base/room_form.html", {"form": form})


@login_required(login_url="login")
def update_room(request, pk):
    room = get_object_or_404(Room, id=pk)
    form = RoomForm(instance=room)

    if request.user is not room.host:
        from django.http import HttpResponse

        return HttpResponse("You're not allowed to be here!")

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
