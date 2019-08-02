from django.urls import path

from shortener.views import ShortenerView, CountShortenerView

urlpatterns = [
    path('', ShortenerView.as_view(), name='index'),
    path('short-link/<slug:short_link>', CountShortenerView.as_view(), name='short_link')
]