from django.db import models


class Goods(models.Model):
    goods_title = models.CharField(max_length=155)
    description = models.SlugField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Goods'
        verbose_name_plural = 'Goods'
    
    def __str__(self):
        return self.goods_title
    
class Question(models.Model):
    question = models.CharField(max_length=155)
    time_created = models.DateField(auto_now_add=True)