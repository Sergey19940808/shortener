from django.urls import path

from register.views import RegisterView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
]