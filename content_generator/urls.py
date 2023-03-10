from django.urls import path
from content_generator import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index_handler),
    path("generate/", views.generate_content),
    path("save/", views.save),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
