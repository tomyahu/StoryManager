from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=50)
    backstory = models.TextField(max_length=10000, default="", blank=True)
    age = models.IntegerField(null=True, blank=True, default=None)
    portrait = models.ImageField(blank=False, default="images/character_portraits/default.png", upload_to='images/character_portraits')

    def __str__(self):
        return self.name

    def get_age(self):
        if self.age == None or self.age == -1:
            return "???"
        elif self.age < -1:
            return "Siempre Existió"
        else:
            return str(self.age)

class CharacterImage(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT, blank=False, null=False)
    image = models.ImageField(blank=False, upload_to='images/character_images')
