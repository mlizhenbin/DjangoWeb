#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)
