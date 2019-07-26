from django.db import models

class Shortener(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    origin_link = models.CharField(max_length=255)
    short_link = models.CharField(max_length=255)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.origin_link}'
