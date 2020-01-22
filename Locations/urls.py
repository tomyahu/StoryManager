from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Locations.views import IndexView, PlaceView, RegionView

urlpatterns = [
    path('', IndexView.as_view()),
    path('place/<int:pk>', PlaceView.as_view()),
    path('region/<int:pk>', RegionView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)