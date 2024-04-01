from django.shortcuts import render , get_object_or_404,redirect
from .models import Meetings , Room

# Create your views here.
def detail(request , id):
    meeting = meetings_planner.objects.get(pk=id)
    return render (request , "meetings/detail. html", {" meeting": meeting})

def detail(request  , id):
    meeting = get_object_or_404(meeting,id)
    return render (request , "meetings/detail.html", {" meeting": meeting})