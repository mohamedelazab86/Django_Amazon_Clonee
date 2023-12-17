# Generated by Django 4.2 on 2023-12-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name_product')),
                ('flag', models.CharField(choices=[('New', 'New'), ('Sale', 'Sale'), ('Feature', 'Feature')], max_length=50, verbose_name='flag')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price')),
                ('image', models.ImageField(upload_to='photo_product/%y-%m-%d', verbose_name='image')),
                ('sku', models.IntegerField(unique=True, verbose_name='sku')),
                ('subtitle', models.TextField(max_length=5000, verbose_name='subtitle')),
                ('description', models.TextField(max_length=50000, verbose_name='descriptions')),
                ('slug', models.CharField(blank=True, max_length=500, null=True, verbose_name='slug')),
            ],
        ),
    ]
