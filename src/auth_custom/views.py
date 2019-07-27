from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class RegisterView(FormView):
    form_class = UserCreationForm

    success_url = '/auth_custom/login/'

    template_name = 'register/register.html'

    def form_valid(self, form):
        form.save()

        return super(RegisterView, self).form_valid(form)