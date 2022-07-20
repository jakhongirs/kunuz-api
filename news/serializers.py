from rest_framework import serializers
from .models import News, Tag, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = News
        fields = "__all__"
