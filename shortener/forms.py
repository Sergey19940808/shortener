from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.core.exceptions import ValidationError

from shortener.models import Shortener


class ShortenerForm(forms.ModelForm):
    class Meta:
        model = Shortener
        fields = ['origin_link']

    def clean_origin_link(self):
        user, origin_link = self.data.get('user'), self.data.get('origin_link')
        if Shortener.objects.filter(
                user_id=self.data.get('user'),
                origin_link=self.data.get('origin_link')
        ).exists():
            raise ValidationError(
                'Добавляемая ссылка уже существует'
            )
        else:
            return origin_link

    def save_model(self, user):
        return self.instance.save(**{'user': user})


