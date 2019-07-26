from django.views.generic.list import ListView

from shortener.models import Shortener


class IndexView(ListView):
    model = Shortener
    template_name = 'shortener/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
