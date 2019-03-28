import json
from django.test import TestCase, Client
from django.urls import reverse
from .serializers import ClotheSerializer
from .models import Clothe
from rest_framework import status

# Create your tests here.
client = Client()

class ClotheTest(TestCase):
    """Test module for Clothe model"""
    def setUp(self):
        Clothe.objects.create(
            name='Shorts', years=4, clad_type='Main Clad', color='brown and black'
        )
        Clothe.objects.create(
            name='Belt', years=1, clad_type='Accessory Clad', color='olive green'
        )
    def test_clothe_clad_type(self):
        clothe_shorts = Clothe.objects.get(name='Shorts')
        clothe_belt = Clothe.objects.get(name='Belt')
        self.assertEqual(
            clothe_shorts.get_clad_type(), "Shorts is a Main Clad."
        )
        self.assertEqual(
            clothe_belt.get_clad_type(), "Belt is a Accessory Clad."
        )

class CreateNewClotheTest(TestCase):
    """Test module for inserting a new clothe"""
    def setUp(self):
        self.valid_payload = {
            'name': 'Shoes',
            'years': 4,
            'clad_type': 'Accessory Clad',
            'color': 'Black'
        }
        self.invalid_payload = {
            'name': '',
            'years': 4,
            'clad_type': 'Fad Clad',
            'color': 'White'
        }
    def test_create_valid_clothe(self):
        response = client.post(
            reverse('get_post_clothes'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_clothe(self):
        response = client.post(
            reverse('get_post_clothes'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetAllClothesTest(TestCase):
    """Test module for GET all clothes API"""
    def setUp(self):
        Clothe.objects.create(
            name='Towel', years=3, clad_type='Bath Clad', color='Blonde'
        )
        Clothe.objects.create(
            name='Longs', years=1, clad_type='Main Clad', color='Brown'
        )
        Clothe.objects.create(
            name='Scrubber', years=2, clad_type='Bath Clad', color='Black'
        )
        Clothe.objects.create(
            name='Tie', years=6, clad_type='Fad Clad', color='Pink and Yellow'
        )
    def test_get_all_clothes(self):
        # get API response
        response = client.get(reverse('get_post_clothes'))
        # get data from db
        clothes = Clothe.objects.all()
        serializer = ClotheSerializer(clothes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleClotheTest(TestCase):
    
    def setUp(self):
        self.lavender = Clothe.objects.create(
            name='Handkerchief', years=2, clad_type='Fad Clad', color='Grey'
        )
    
    def test_get_valid_single_clothe(self):
        response = client.get(
            reverse('get_delete_update_clothes', kwargs={'pk': self.lavender.pk})
        )
        clothe = Clothe.objects.get(pk=self.lavender.pk)
        serializer = ClotheSerializer(clothe)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_clothe(self):
        response = client.get(
            reverse('get_delete_update_clothes', kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class UpdateSingleClotheTest(TestCase):
    """Test module for updating an existing clothe record"""

    def setUp(self):
        self.demetrius = Clothe.objects.create(
            name='Ring', years=3, clad_type='Fad Clad', color='Gold'
        )
        self.neoptalamus = Clothe.objects.create(
            name='Sheets', years=1, clad_type='Sleep Clad', color='White'
        )
        self.valid_payload = {
            'name': 'Bag',
            'years': 2,
            'clad_type': 'Accessory Clad',
            'color': 'Black'
        }
        self.invalid_payload = {
            'name': '',
            'years': 4,
            'clad_type': 'Fad Clad',
            'color': 'White'
        }
    def test_valid_update_clothe(self):
        response = client.put(
            reverse('get_delete_update_clothes', kwargs={'pk': self.neoptalamus.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    def test_invalid_update_clothe(self):
        response = client.put(
            reverse('get_delete_update_clothes', kwargs={'pk': self.demetrius.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleClotheTest(TestCase):
    """Test module for deleting an existing clothe record"""
    def setUp(self):
        self.demetrius = Clothe.objects.create(
            name='Ring', years=3, clad_type='Fad Clad', color='Gold'
        )
        self.neoptalamus = Clothe.objects.create(
            name='Sheets', years=1, clad_type='Sleep Clad', color='White'
        )
    def test_valid_delete_clothe(self):
        response = client.delete(
            reverse('get_delete_update_clothes', kwargs={'pk': self.demetrius.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    def test_invalid_delete_clothe(self):
        response = client.delete(
            reverse('get_delete_update_clothes', kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)