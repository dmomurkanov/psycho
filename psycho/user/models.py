from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
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

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
