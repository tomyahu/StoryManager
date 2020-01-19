from django.contrib import admin

# Register your models here.
from Characters.models import Character, CharacterImage

admin.site.register(Character)
admin.site.register(CharacterImage)