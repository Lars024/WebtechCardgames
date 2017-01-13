from django import forms
from .model import Room

class createRoomForm(forms.form):
	name = forms.textField()