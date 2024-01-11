# Generated by Django 4.2.1 on 2024-01-10 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Катеория',
                'verbose_name_plural': 'Катеории',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описании')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Скидка в %')),
                ('quanity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'product',
            },
        ),
    ]
