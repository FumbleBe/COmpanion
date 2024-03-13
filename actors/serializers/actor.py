from rest_framework import serializers

from actors.models import *


class CharacterListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = '__all__'


# class ProductDetailSerializer(serializers.ModelSerializer):

#     articles = serializers.SerializerMethodField()

#     class Meta:
#         model = Actor
#         fields = ["id", "date_created", "date_updated", "name", "category", "articles"]

#     def get_articles(self, instance):
#         queryset = instance.articles.filter(active=True)
#         serializer = ArticleSerializer(queryset, many=True)
#         return serializer.data
