from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=256)


class OrthostaticTest(models.Model):
    date = models.DateTimeField()
    first_heart_rate = models.IntegerField()
    second_heart_rate = models.IntegerField()
    result = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)