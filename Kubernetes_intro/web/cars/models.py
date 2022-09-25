from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Car(models.Model):
        id = models.AutoField(primary_key=True)
        vin = models.CharField(verbose_name='VinNum', unique=True, db_index=True, max_length=64)
        color = models.CharField(verbose_name='Color', db_index=True, max_length=64)
        brand = models.CharField(verbose_name='brand', db_index=True, max_length=64)
        CAR_TYPES = (
            (1, 'Хатчбек'),
            (2, 'Седан'),
            (3, 'Баклажан'),
            (4, 'Лилипут'),
        )
        car_type = models.IntegerField(verbose_name='Car_Type', choices=CAR_TYPES )
        user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)