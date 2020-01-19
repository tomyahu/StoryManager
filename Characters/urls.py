from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Characters.views import IndexView, CharacterView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:pk>', CharacterView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)