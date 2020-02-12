from StoryManager.consts import PROJECT_NAME

from django.views.generic import TemplateView
from Items.models import Item, ItemImage


class IndexView(TemplateView):
    template_name = "items_overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = PROJECT_NAME
        context["items"] = Item.objects.all()
        return context


class ItemView(TemplateView):
    template_name = "item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = PROJECT_NAME

        current_item = Item.objects.get(id=kwargs["pk"])
        context["item"] = current_item
        context["item_images"] = ItemImage.objects.filter(item=current_item)
        return context
