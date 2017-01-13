from django.db import models


# Create your models here.
class Room(models.Model):
	name = models.TextField()
	label = models.SlugField(unique=True)

	def __unicode__(self):
		return self.label

	def __str__(self):
		return self.name

class Player:
	room = models.ForeignKey(Room, related_name='player')
	name = models.TextField()
