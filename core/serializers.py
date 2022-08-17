from cgitb import lookup
from rest_framework import serializers
from .models import Article, Author, Category


class ArticleSerializer(serializers.ModelSerializer):
    related_articles  = serializers.StringRelatedField(many=True)
    class Meta:
        model = Article
        fields = '__all__'
        lookup_field = 'slug'

class AuthorSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = '__all__'