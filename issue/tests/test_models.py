from django.test import TestCase

from user.models import User
from ..models import Person, Position, Department, Team


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        position = Position.objects.create(name='Kierownik')
        department = Department.objects.create(name='IT')
        user = User.objects.create(first_name='Jan', last_name='Kowalski', email='ww@wp.pl', department=department)
        team = Team.objects.create(name='Drużyna', country="PL")
        Person.objects.create(name='Jan', sex=Person.SexType.MAN, position=position, owner=user, team=team)

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('name').max_length
        self.assertEqual(max_length, 64)