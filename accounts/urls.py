from django.urls import path

from accounts.views import RegisterView, LogoutViewCustom, LoginViewCustom

urlpatterns = [
    path('', RegisterView.as_view(), name='register_custom'),
    path('logout/', LogoutViewCustom.as_view(), name='logout_custom'),
    path('login/', LoginViewCustom.as_view(), name='login_custom')
]