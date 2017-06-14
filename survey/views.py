# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import (
    mixins,
    generics,
    status
)
from rest_framework.response import Response

from survey import models
from survey.serializers import (
    PersonSerializer,
    RefTokenSerializer,
    RefQuestionSerializer,
    TokenSerializer,
)


class RefTokenList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = models.RefToken.objects.all()
    serializer_class = RefTokenSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TokenList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = models.Token.objects.all()
    serializer_class = TokenSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TokenDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = models.Token.objects.all()
    serializer_class = TokenSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RefQuestionList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):

    queryset = models.RefQuestion.objects.all()
    serializer_class = RefQuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RefQuestionDetail(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = models.RefQuestion.objects.all()
    serializer_class = RefQuestionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RefTokenDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = models.RefToken.objects.all()
    serializer_class = RefTokenSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PersonList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):

    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PersonDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'user__username'

    def _raise_error(self, message, status_code):
        return Response(
            {'Error': message},
            status=status_code
        )

    def _submit_answer(self, question, answer='no'):
        # questions = data.get('questions')
        for token in question.get('tokens'):
            try:
                t = models.Token.objects.get(attribute__id=token.get('id'))
                if answer in ('yes', 'YES'):
                    t.yes += token.get('yes')
                else:
                    t.no += token.get('no')
                t.save()
            except Exception:
                pass
        return Response(answer)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return data

    def get(self, request, *args, **kwargs):
        return Response(self.retrieve(request, *args, **kwargs))

    def post(self, request, *args, **kwargs):
        data = self.retrieve(request, *args, **kwargs)
        if 'question_id' in kwargs.keys() and 'answer' in kwargs.keys():
            question = next(iter(filter(
                lambda x: str(x.get('id')) == kwargs.get('question_id'),
                data.get('questions'))), None)
            if question:
                return self._submit_answer(question, kwargs.get('answer'))
            return self._raise_error(
                "Question not found",
                status.HTTP_404_NOT_FOUND
            )
        return Response(data)

    def delete(self, request, *args, **kwargs):
        """DELETE Person
            http DELETE /users/<username>/
        """
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


def index(request):
    return render(request, "index.html", {
        "integer_values": models.Token.objects.order_by('id')
    })
