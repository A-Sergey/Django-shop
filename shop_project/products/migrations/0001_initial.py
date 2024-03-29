# Generated by Django 4.0.4 on 2022-09-19 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('name_lower', models.CharField(editable=False, max_length=20)),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('price', models.CharField(max_length=10)),
                ('sell', models.CharField(blank=True, default='', max_length=10)),
                ('description', models.CharField(max_length=300)),
                ('quantity', models.IntegerField(default=0)),
                ('image', models.ImageField(default='images/noImage.png', upload_to='images/')),
                ('product_of_the_day', models.BooleanField(default=False)),
                ('visible_in_shop', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.product')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
