from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Blog

User = get_user_model()


class BlogSerializers(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Blog
        fields = ['author', 'title', 'content']

    def get_author(self, obj):
        request = self.context['request']
        email = request.user.email
        return email

    def create(self, validated_data):
        email = self.get_author(self.instance)
        author = User.objects.get(email=email)
        validated_data['author'] = author
        blog = Blog.objects.create(**validated_data)
        return blog
