# encoding:utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('姓名',max_length=100,blank=True)
    apg = models.CharField('年龄',max_length=100,blank=True)
    