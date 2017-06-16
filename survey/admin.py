# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models


class RefTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'yes', 'no')


class RefQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class TokenAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'value')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'associated_questions')

    def associated_questions(self, obj):
        return ', '.join([question.title for question in obj.questions.all()])


admin.site.register(models.RefToken, RefTokenAdmin)
admin.site.register(models.Token, TokenAdmin)
admin.site.register(models.RefQuestion, RefQuestionAdmin)
admin.site.register(models.Person, PersonAdmin)
