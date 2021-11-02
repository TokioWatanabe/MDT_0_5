from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

"""
Item
    # storage
    # group
    # lot
    # status
    # remaining
    # unit
    # records
        # datetime
        # operator
        # purpose
        # use_qty
        # rem_qty


    # make_record
    # modify_record
    # show_record
"""

class Item(models.Model):
    storage = models.CharField(max_length=10)
    group = models.CharField(max_length=20)
    lot = models.CharField(max_length=20)
    status = models.CharField(max_length=15)
    remaining = models.FloatField()
    unit = models.CharField(max_length=8)

    def store(self):
        self.save()

    def __str__(self):
        return self.group