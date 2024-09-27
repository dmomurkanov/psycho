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
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['my_order']

