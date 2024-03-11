from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group

'''
==> self.client: An instance of APIClient for making requests to the API.
==> self.user: A test user created with the username 'testuser' and password 'testpassword'.
==> self.manager_group: A test group created with the name 'Manager'.
==> self.stream_data: A list data for creating a stream. In this case, it contains a key 'stream_name' with the value 'cse'.
'''
class StreamCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.manager_group = Group.objects.create(name='Manager')
        self.stream_data = {'stream_name': 'cse'}

    def test_create_stream_with_manager_permission(self):
        self.user.groups.add(self.manager_group)# assigns the user to the 'Manager' group.
        self.client.force_authenticate(user=self.user)# authenticates the test client as the specified user.
        response = self.client.post(reverse('stream-create'), self.stream_data, format='json')# sends a POST request to the URL
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)# asserts that the response status code is equal to 201 CREATED or Not.

    def test_create_stream_without_manager_permission(self):
        self.client.force_authenticate(user=self.user)# authenticates the test client as the specified user.
        response = self.client.post(reverse('stream-create'), self.stream_data, format='json')# sends a POST request to the URL associated with the name 
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)# line asserts that the response status code is equal to 403 FORBIDDEN.

    def test_create_stream_unauthenticated(self):
        response = self.client.post(reverse('stream-create'), self.stream_data, format='json')# Sends the post request to the specified url.
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)# line asserts that the response status code is equal to 403 FORBIDDEN.
