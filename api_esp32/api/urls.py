from django.urls import path
from .views import Esp32View

urlpatterns = [
    path('esp32', Esp32View.as_view(), name='esp32_list')
]