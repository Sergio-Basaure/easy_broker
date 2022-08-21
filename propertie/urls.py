from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "propertie"
urlpatterns = [
    path("", home, name = 'index'),
    path('propertie/<str:id>', detail_propertie, name = 'detail_propertie'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

