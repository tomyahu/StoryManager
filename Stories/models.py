from django.db import models

from Characters.models import Character
from Items.models import Item
from Locations.models import Place


class Story(models.Model):
    name = models.CharField(max_length=50)
    story = models.TextField(max_length=100000, default="", blank=True)

    def __str__(self):
        return self.name

class CharacterInStory(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT, blank=False, null=False)
    story = models.ForeignKey(Story, on_delete=models.PROTECT, blank=False, null=False)

class PlaceInStory(models.Model):
    place = models.ForeignKey(Place, on_delete=models.PROTECT, blank=False, null=False)
    story = models.ForeignKey(Story, on_delete=models.PROTECT, blank=False, null=False)

class ItemInStory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, blank=False, null=False)
    story = models.ForeignKey(Story, on_delete=models.PROTECT, blank=False, null=False)