from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name