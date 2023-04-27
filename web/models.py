from django.db import models
from django.db.models import Case, Value, When
from django.contrib.auth import get_user_model


# class User(models.Model):
#     MALE = 'муж.'
#     FEMALE = 'жен.'
#
#     CHOICES = (
#         (MALE, 'муж.'),
#         (FEMALE, 'жен.'),
#     )
#     name = models.CharField(max_length=64)
#     surname = models.CharField(max_length=64)
#     email = models.CharField(max_length=256)
#     pasword = models.CharField(max_length=256)
#     date_of_birth = models.DateField()
#     sex = models.CharField(max_length=255, choices=CHOICES, default=FEMALE)

User = get_user_model()

class Measurement(models.Model):
    date = models.DateTimeField()
    height = models.IntegerField()
    weight = models.IntegerField()
    heart_rate = models.IntegerField()
    imt = models.FloatField()
    target_heart_rate = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrthostaticTest(models.Model):
    date = models.DateTimeField()
    first_heart_rate = models.IntegerField()
    second_heart_rate = models.IntegerField()
    result = second_heart_rate - first_heart_rate
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class RuffierTest(models.Model):
    date = models.DateTimeField()
    first_heart_rate = models.IntegerField()
    second_heart_rate = models.IntegerField()
    third_heart_rate = models.IntegerField()
    result = ((first_heart_rate + second_heart_rate + third_heart_rate) * 4 - 200) /10
    user = models.ForeignKey(User, on_delete=models.CASCADE)