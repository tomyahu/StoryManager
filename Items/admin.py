from django.contrib import admin

# Register your models here.
from Items.models import Item, ItemImage

admin.site.register(Item)
admin.site.register(ItemImage)