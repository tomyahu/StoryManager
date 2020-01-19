from StoryManager.consts import PROJECT_NAME
from django.shortcuts import render

from django.views.generic import TemplateView
from Characters.models import Character, CharacterImage

class IndexView(TemplateView):
    template_name = "character_overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = PROJECT_NAME
        context["characters"] = Character.objects.all()
        return context

class CharacterView(TemplateView):
    template_name = "character.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = PROJECT_NAME
        context["character"] = Character.objects.get(id=kwargs["pk"])
        context["character_images"] = CharacterImage.objects.filter(character=context["character"])
        return context