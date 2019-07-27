from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from shortener.models import Shortener
from shortener.forms import ShortenerForm


class IndexView(LoginRequiredMixin, ListView):
    model = Shortener
    template_name = 'shortener/index.html'

    def get(self, request, *args, **kwargs):
        form = ShortenerForm()
        context = self._get_context(request, form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwarg):
        form = ShortenerForm(request.POST)
        context = self._get_context(request, form)
        if form.is_valid():
            form.save_model(request.user)
            return redirect('/')
        else:
            return render(request, self.template_name, context)

    def _get_context(self, request, form):
        shorteners = Shortener.objects.filter(user=request.user)
        context = {
            'title': 'Главная',
            'shorteners': self.get_page(shorteners, request),
            'form': form,
            'count': len(shorteners)
        }
        return context

    def get_page(self, shorteners, request):
        paginator = Paginator(shorteners, 1)

        page = request.GET.get('page')
        return paginator.get_page(page)


