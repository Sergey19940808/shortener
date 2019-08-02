from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
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
        context = self.service_class.get_context(request, form)
        if request.session.get('short_link'):
            context.update({'short_link': request.session.get('short_link')})
            request.session.pop('short_link')
        elif request.session.get('origin_link'):
            context.update({'origin_link': request.session.get('origin_link')})
            request.session.pop('origin_link')
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


class CountShortenerView(LoginRequiredMixin, DetailView):
    queryset = Shortener.objects.all()

    def get(self, request, *args, **kwargs):
        shortener = Shortener.objects.get(
            user=request.user,
            short_link=kwargs.get('short_link')
        )
        shortener.count += 1
        shortener.save()
        request.session['origin_link'] = shortener.origin_link
        return redirect('index')

    def get_object(self, queryset=queryset):
        return queryset.get(short_link=self.kwargs.get('short_link'))



