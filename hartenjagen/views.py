from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Room
from .form import createRoomForm

# Create your views here.
def index(request):
	roomList = Room
	return render(request, 'hartenjagen/rooms.html', {'roomList': roomList})
	
	
def createRoom(request):
	if request.method == 'POST':
		form = createRoomForm(request.POST)
		Room_obj = Room( name = str(request.post.get('roomName', 'error'))
		Room_obj.save()
	roomList = Room.order_by('name')
	return render(request, 'hartenjagen/rooms.html', {'roomList': roomList})