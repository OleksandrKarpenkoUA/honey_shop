from django.db import models

class Goods(models.Model):
    title = models.CharField(max_length=155, default='Honey')
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Goods'
        verbose_name_plural = 'Goods'
        
    def __str__(self):
        return self.title