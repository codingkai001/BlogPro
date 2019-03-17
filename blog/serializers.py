from rest_framework import serializers
from .models import Blog, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'author', 'body', 'publish_date', 'read_nums', 'category')
