from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationUserTestCase(APITestCase):
    
    def setUp(self):
        
        self.list_url = reverse('programs-list')
        self.user = User.objects.create_user('c3po', password='12345') # integration tests need database, that's why we use .objects
    
    def test_authentication_user_with_correct_credentials(self):
        """Test that verifies the authentication of an user with the correct credentials"""
        user = authenticate(username = 'c3po', password = '12345')
        self.assertTrue(user is not None and user.is_authenticated)
        
    def test_authentication_user_with_INcorrect_username(self):
        """Test that verifies the authentication of an user with the incorrect username"""
        user = authenticate(username = 'c4po', password = '12345')
        self.assertFalse(user is not None and user.is_authenticated)
        
    def test_authentication_user_with_INcorrect_password(self):
        """Test that verifies the authentication of an user with the incorrect password"""
        user = authenticate(username = 'c3po', password = '123456')
        self.assertFalse(user is not None and user.is_authenticated)
        
    def test_GET_requisition_unauthorized(self):
        """Test that verifies a GET requisition unauthorized"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_GET_requisition_with_authenticated_user(self):
        """Test that verifies a GET requisition of an authorized user"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        
        