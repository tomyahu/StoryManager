from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Stories.views import IndexView, StoryView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:pk>', StoryView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)