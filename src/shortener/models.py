from hashlib import sha256
from django.db import models
from django.contrib.auth.models import User

class Shortener(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    origin_link = models.URLField(max_length=255, verbose_name='Оригинальная ссылка', unique=True)
    short_link = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if kwargs and kwargs.get('user'):
            self.user = kwargs.pop('user')
        hash_link = sha256()
        hash_link.update(self.origin_link.encode('utf-8'))
        self.short_link = f'short/{hash_link.hexdigest()[:10]}'
        return super(Shortener, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.origin_link}'
