from django.test import TestCase
from selenium import webdriver
from django.urls import reverse
from .models import Poodle
from organizer.models import Kennel, Person
from django.utils import timezone


class HomeTests(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_home_exists(self):
        url = "http://localhost:8000" + reverse('poodles:home')
        self.browser.get(url)
        self.assertIn('Welcome', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()


class PoodleListTests(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_list_exists(self):
        url = "http://localhost:8000" + reverse('poodles:poodles')
        self.browser.get(url)
        self.assertIn('Poodles', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()


class PoodleModelTests(TestCase):
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

    def create_poodle(self):
        return Poodle.objects.create(
            name_call='TestCallName',
            name_registered='TestRegName',
            sex='M', color="U",
            akc="testAKC",
            person_owner=self.create_person(),
            person_breeder=self.create_person(),
            poodle_sire=self.create_poodle(),
            poodle_dam=self.create_poodle(),
            created_at=timezone.now)

    def test_Poodle_creation(self):
        w = self.create_poodle()
        self.assertTrue(isinstance(w, Poodle))
        self.assertTrue(isinstance(w.poodle_sire, Poodle))
        self.assertTrue(isinstance(w.poodle_dam, Poodle))
        self.assertTrue(isinstance(w.person_owner, Person))
        self.assertTrue(isinstance(w.person_breeder, Person))
