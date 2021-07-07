from rest_framework import serializers

from films.models import Category, Film, FilmSession, Hall


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FilmSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Film
        fields = "__all__"


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = "__all__"


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
