from django.urls import path

from auth_custom.views import RegisterView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
]