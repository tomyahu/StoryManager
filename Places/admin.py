from django.contrib import admin

# Register your models here.
from Places.models import Region, Place, PlaceImage

admin.site.register(Region)
admin.site.register(Place)
admin.site.register(PlaceImage)