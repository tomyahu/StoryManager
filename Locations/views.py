from Locations.models import Place, Region, PlaceImage
from StoryManager.consts import PROJECT_NAME
from django.shortcuts import render

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "locations_overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = PROJECT_NAME
        context["places"] = Place.objects.all()
        context["regions"] = Region.objects.all()
        return context

class PlaceView(TemplateView):
    template_name = "place.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = PROJECT_NAME
        context["place"] = Place.objects.get(id=kwargs["pk"])
        context["place_images"] = PlaceImage.objects.filter(place=context["place"])
        return context

class RegionView(TemplateView):
    template_name = "region.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = PROJECT_NAME
        context["region"] = Region.objects.get(id=kwargs["pk"])
        return context