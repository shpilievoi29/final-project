"""

Implemented Test Cases for  Film application

"""

from django.test import TestCase

from films.models import Category, Film, Hall

"""
Category model test case

"""


class CategoryTestCase(TestCase):
    def test_string_representation(self):
        category = Category(category="My category")
        self.assertEqual(str(category), category.category)


"""

Film model test case

"""


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


"""

Hall model test case

"""


class HallModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.hall = Hall.objects.create(
            hall="Yellow"
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.hall.hall, str)
