from rest_framework import serializers
from survey import models


class RefTokenSerializer(serializers.ModelSerializer):

    token = serializers.CharField(required=True, max_length=255)
    yes = serializers.IntegerField(required=True)
    no = serializers.IntegerField(required=True)

    class Meta:
        model = models.RefToken
        fields = ('id', 'token', 'yes', 'no')


class TokenSerializer(serializers.ModelSerializer):

    attribute = RefTokenSerializer(
        many=False,
        read_only=True)

    class Meta:
        model = models.Token
        fields = ('attribute', 'yes', 'no')


class RefQuestionSerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=True, max_length=255)
    tokens = RefTokenSerializer(many=True, read_only=True)

    class Meta:
        model = models.RefQuestion
        fields = ('id', 'title', 'tokens')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    questions = RefQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Person
        fields = ('user', 'questions')

    def create(self, validated_data):
        return models.Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return 'Hello'
