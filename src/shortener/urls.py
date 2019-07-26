from django.urls import path

from shortener.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]