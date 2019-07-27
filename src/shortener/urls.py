from django.urls import path

from shortener.views import ShortenerView, CountShortenerView

urlpatterns = [
    path('', ShortenerView.as_view(), name='index'),
    path('count/<int:pk>', CountShortenerView.as_view(), name='count')
]