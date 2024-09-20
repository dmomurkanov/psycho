from django.db import models

# Create your models here.
class Questions(models.Model):
    high_schoolers_questions = models.CharField(max_length=150)
    student_questions = models.CharField(max_length=150)
    adults_questions = models.CharField(max_length=150)
