from Stories.models import Story, CharacterInStory, PlaceInStory, ItemInStory, StoryImage
from StoryManager.consts import PROJECT_NAME
from django.shortcuts import render

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "stories_overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = PROJECT_NAME
        context["stories"] = Story.objects.all()
        return context

class StoryView(TemplateView):
    template_name = "story.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = PROJECT_NAME

        current_story = Story.objects.get(id=kwargs["pk"])
        context["story"] = current_story
        context["story_images"] = StoryImage.objects.filter(story=current_story)
        context["related_characters"] = CharacterInStory.objects.filter(story=current_story)
        context["related_places"] = PlaceInStory.objects.filter(story=current_story)
        context["related_items"] = ItemInStory.objects.filter(story=current_story)
        return context