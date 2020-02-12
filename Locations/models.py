from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50)
    story = models.TextField(max_length=10000, default="", blank=True)
    image = models.ImageField(blank=False, default="images/region_images/default.png", upload_to='images/region_images')

    def __str__(self):
        return self.name

    def get_story_as_patagraph_list(self):
        return self.story.split("\n")

class Place(models.Model):
    name = models.CharField(max_length=50)
    story = models.TextField(max_length=10000, default="", blank=True)
    foundation = models.IntegerField(blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.PROTECT, blank=False, null=False)
    image = models.ImageField(blank=False, upload_to='images/place_images')