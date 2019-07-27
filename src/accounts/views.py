from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView,LoginView

class RegisterView(FormView):
    form_class = UserCreationForm

    success_url = '/accounts/login/'

    template_name = 'accounts/register.html'

    def form_valid(self, form):
        form.save()

        return super(RegisterView, self).form_valid(form)

class LogoutViewCustom(LogoutView):
    template_name = 'accounts/logged_out.html'

class LoginViewCustom(LoginView):
    template_name = 'accounts/login.html'