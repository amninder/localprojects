# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from channels.binding.websockets import WebsocketBinding


class RefToken(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False,
        unique=True)
    token = models.CharField(max_length=255, blank=False)
    yes = models.IntegerField(blank=False)
    no = models.IntegerField(blank=False)

    def __str__(self):
        return self.token

    class Meta:
        verbose_name = _('Token Reference')
        ordering = ('token',)


class Token(models.Model):
    attribute = models.ForeignKey(RefToken, related_name='attribute')
    yes = models.IntegerField(default=0)
    no = models.IntegerField(default=0)

    def __str__(self):
        return self.attribute.token

    class Meta:
        verbose_name = _('Token')
        ordering = ('attribute',)


class RefQuestion(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False,
        unique=True)
    title = models.CharField(max_length=255, blank=False)
    tokens = models.ManyToManyField(RefToken)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Question Reference')
        ordering = ('title',)


class Person(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)
    questions = models.ManyToManyField(RefQuestion)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('User Profile')


class IntegerValueBinding(WebsocketBinding):

    model = Token
    stream = "intval"
    fields = ["attribute", "yes", "no"]

    @classmethod
    def group_names(cls, *args, **kwargs):
        return ['binding.values']

    def has_permission(self, user, action, pk):
        return True
