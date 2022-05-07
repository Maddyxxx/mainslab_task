from django.test import TestCase
from .models import Client


class OrganizationTest(TestCase):
    def setUp(self):
        self.client = Client(client_name='test_client_name')
        self.client.save()
        self.organization_name = 'test_organization_name'

    def tearDown(self):
        self.client.delete()

    def test_read_organization(self):
        self.assertEqual(self.organization_name, 'test_organization_name')
        self.assertEqual(self.client.client_name, 'test_client_name')

