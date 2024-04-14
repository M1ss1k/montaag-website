from django.db import models

class LogisticsTariffs(models.Model):
    title = models.CharField(verbose_name="Название тарифа", max_length=150)
    description = models.TextField(verbose_name="Описание тарифа")
    price = models.CharField(verbose_name="Цена тарифа", max_length=50)
    image = models.ImageField(verbose_name="Фото тарифа", upload_to='photos/tariffs')

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
# Create your models here.

class LogisticsOrders(models.Model):

    CHOICES = (
        ('EASE', "EASE - Меньше 100 кг."),
        ("MEDIUM", "MEDIUM - От 100 до 1000 кг."),
        ('HEAVY', "HEAVY - От 1т. и более."),
        ('SPECIAL DELIVERY', "Специальная доставка."),
        ("Инкассация", "Перевозка денег."),


    )
    name = models.CharField(verbose_name="Имя заказчика", max_length=150)
    order_contact = models.CharField(verbose_name="Контакты ( почта или ник в дискорде )", max_length=250)
    order_description = models.TextField(verbose_name="Описание заказа, что нужно перевезти, вес груза, условия перевозки.")
    order_tariff = models.CharField(verbose_name="Тариф заказа", choices=CHOICES, max_length=150)
    order_to = models.CharField(verbose_name="Пункт назначения", max_length=150)
    order_time = models.DateTimeField(verbose_name="Время заказа", auto_now_add=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"