from Stories.models import Story
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