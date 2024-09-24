from Tools.demo.mcast import sender
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=150, null=True)
    HIGH_SCHOOLER = "Школьник(-ца)"
    STUDENT = "Студент"
    ADULT = "Взрослый(-ая)"
    SOCIAL_STATUS = (
        (HIGH_SCHOOLER, "Школьник(-ца)"),
        (STUDENT, "Студент"),
        (ADULT, "Взрослый(-ая)")
    )
    phone_number = models.CharField("Номер телефона", max_length=13, unique=True, null=True, blank=True)
    age = models.IntegerField("Возраст")
    social_status = models.CharField("Социальный статус", choices=SOCIAL_STATUS)
    school = models.CharField("Учебное заведение:", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

