from django.core.paginator import Paginator

from shortener.models import Shortener


class ShortenerService(object):
    @staticmethod
    def _get_page(shorteners, request):
        paginator = Paginator(shorteners, 10)

        page = request.GET.get('page')
        return paginator.get_page(page)

    def get_context(self, request, form):
        shorteners = Shortener.objects.filter(user=request.user)
        context = {
            'title': 'Главная',
            'shorteners': self._get_page(shorteners, request),
            'form': form,
            'count': len(shorteners)
        }
        return context