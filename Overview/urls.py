from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Overview.views import OverviewView

urlpatterns = [
    path('', OverviewView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)