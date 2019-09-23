from django.db import models
DEFAULT_STATUS = 'other'
STATUS_CHOICES = [(DEFAULT_STATUS, 'Разное'), ('food', 'Еда'), ('car','Машина'), ('drink','Напиток'), ('electronik','Электроника')]

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=20, null=False, default=DEFAULT_STATUS, blank=False, verbose_name='Категория', choices=STATUS_CHOICES)
    balance = models.PositiveIntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'