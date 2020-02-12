from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Items.views import IndexView, ItemView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:pk>', ItemView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)