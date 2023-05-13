from django.db import models
from django.urls import reverse

# Create your models here.

class List(models.Model):
    """список"""
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """элемент списка"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.text

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')
