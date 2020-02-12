from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=10000, default="", blank=True)
    display = models.ImageField(blank=False, default="images/item_displays/default.png", upload_to='images/item_displays')

    def __str__(self):
        return self.name

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, blank=False, null=False)
    image = models.ImageField(blank=False, upload_to='images/item_images')