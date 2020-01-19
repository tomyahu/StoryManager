from django.shortcuts import render
from StoryManager.consts import PROJECT_NAME

# Create your views here.
from django.views.generic import TemplateView


class OverviewView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = PROJECT_NAME
        return context