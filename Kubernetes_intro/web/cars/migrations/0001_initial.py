# Generated by Django 2.2.12 on 2022-06-28 15:29

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
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='VinNum')),
                ('color', models.CharField(db_index=True, max_length=64, verbose_name='Color')),
                ('brand', models.CharField(db_index=True, max_length=64, verbose_name='brand')),
                ('car_type', models.IntegerField(choices=[(1, 'Хатчбек'), (2, 'Седан'), (3, 'Баклажан'), (4, 'Лилипут')], verbose_name='Car_Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
