from django.http import HttpResponse
from django.views.generic.list import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from shortener.models import Shortener
from shortener.forms import ShortenerForm
from shortener.services import ShortenerService


class ShortenerView(LoginRequiredMixin, ListView):
    model = Shortener
    template_name = 'shortener/index.html'
    service_class = ShortenerService()

    def get(self, request, *args, **kwargs):
        form = ShortenerForm()
        if request.session.get('short_link'):
            context = self.service_class.get_context(request, form, request.session.get('short_link'))
            request.session.pop('short_link')
        else:
            context = self.service_class.get_context(request, form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwarg):
        form = ShortenerForm(request.POST)
        if form.is_valid():
            short_link = form.save_model(request.user)
            request.session['short_link'] = short_link.short_link
            return redirect('index')
        else:
            context = self.service_class.get_context(request, form)
            return render(request, self.template_name, context)


class CountShortenerView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        shortener = Shortener.objects.get(pk=int(kwargs.get('pk')))
        shortener.count += 1
        shortener.save()
        return HttpResponse()


