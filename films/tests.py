from django.test import TestCase

from films.models import Category, Film, Hall


class CategoryTestCase(TestCase):
    def test_string_representation(self):
        category = Category(category="My category")
        self.assertEqual(str(category), category.category)


class FilmTestCase(TestCase):
    def test_string_representation(self):
        film = Film(film_name="Hooray")
        self.assertEqual(str(film), film.film_name)


class FilmModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.film = Film.objects.create(
            film_name="Snatch",
            film_description="Good",
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.film.film_name, str)
        self.assertIsInstance(self.film.film_description, str)


class HallModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.hall = Hall.objects.create(
            hall="Yellow"
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.hall.hall, str)
