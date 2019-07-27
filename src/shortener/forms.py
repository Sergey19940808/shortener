from django import forms

from shortener.models import Shortener


class ShortenerForm(forms.ModelForm):
    class Meta:
        model = Shortener
        fields = ['origin_link']

    def save_model(self, user):
        return self.instance.save(**{'user': user})


