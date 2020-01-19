from django.contrib import admin

# Register your models here.
from Stories.models import Story, PlaceInStory, CharacterInStory, ItemInStory

admin.site.register(Story)
admin.site.register(CharacterInStory)
admin.site.register(PlaceInStory)
admin.site.register(ItemInStory)