"""
Model Film serializer
"""


from rest_framework import serializers

from films.models import Category, Film, FilmSession, Hall

"""

Implemented serializer for model Category


"""


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


"""

Films serializer
"""


class FilmSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Film
        fields = "__all__"


"""
Hall serializer
"""


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = "__all__"


"""

Session serializer

"""


class FilmSessionSerializer(serializers.ModelSerializer):
    film_name = serializers.PrimaryKeyRelatedField(
        queryset=Film.objects.all()
    )
    created_hall = serializers.PrimaryKeyRelatedField(
        queryset=Hall.objects.all()
    )

    class Meta:
        model = FilmSession
        fields = "__all__"
