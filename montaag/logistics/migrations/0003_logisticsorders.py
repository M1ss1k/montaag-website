# Generated by Django 5.0.4 on 2024-04-14 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0002_alter_logisticstariffs_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticsOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя заказчика')),
                ('order_contact', models.CharField(max_length=250, verbose_name='Контакты ( почта или ник в дискорде )')),
                ('order_description', models.TextField(verbose_name='Описание заказа')),
                ('order_tariff', models.CharField(choices=[('EASE', 'EASE - Меньше 100 кг.'), ('MEDIUM', 'MEDIUM - От 100 до 1000 кг.'), ('HEAVY', 'HEAVY - От 1т. и более.'), ('SPECIAL DELIVERY', 'Специальная доставка.'), ('Инкассация', 'Перевозка денег.')], max_length=150, verbose_name='Тариф заказа')),
                ('order_to', models.CharField(max_length=150, verbose_name='Пункт назначения')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='Время заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
