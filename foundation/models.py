from django.db import models


class PhoneBook(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    is_block = models.BooleanField(default=False)
    