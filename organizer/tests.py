from django.test import TestCase
from selenium import webdriver
from .models import Kennel, Person
from .forms import CrispyKennelForm, CrispyPersonForm
from django.urls import reverse
from django.utils import timezone


class PersonListTests(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_list_exists(self):
        url = "http://localhost:8000" + reverse('organizer:people')
        self.browser.get(url)
        self.assertIn('People', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()


class PersonModelTests(TestCase):
    def create_kennel(self):
        return Kennel.objects.create(
            name="TestKennelName",
            created_at=timezone.now)

    def create_person(self):
        return Person.objects.create(
            last_name='TestLastName',
            first_name='TestFirstName',
            mi='M', kennel=self.create_kennel(),
            created_at=timezone.now)

    def test_person_creation(self):
        w = self.create_person()
        self.assertTrue(isinstance(w, Person))
        self.assertTrue(isinstance(w.kennel, Kennel))
