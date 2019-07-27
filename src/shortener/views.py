from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from shortener.models import Shortener


class IndexView(LoginRequiredMixin, ListView):
    model = Shortener
    template_name = 'shortener/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
