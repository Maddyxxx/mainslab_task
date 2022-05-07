from collections import OrderedDict
from datetime import datetime
from django.test import TestCase
from bills.models import Bill
from clients.models import Organization, Client


class BillTest(TestCase):
    def setUp(self):
        test_client = Client(client_name='test_client_name')
        test_client.save()
        self.client_org = Organization(
            client=test_client,
            organization_name='test_organization_name'
        )
        self.client_org.save()
        self.bill_number = 5
        self.bill_sum = 123
        self.bill_date = datetime.now()

    def tearDown(self):
        self.client_org.delete()

    def test_read_bill(self):
        self.assertEqual(self.client_org.organization_name, 'test_organization_name')
        self.assertEqual(self.client_org.client.client_name, 'test_client_name')
        self.assertEqual(self.bill_number, 5)
        self.assertEqual(self.bill_sum, 123)

    def test_no_bill(self):
        response = self.client.get('/bills/')
        self.assertEqual(response.data['bills'], [])

    def test_one_bill(self):
        self.bill1 = Bill(
            client_org=self.client_org,
            bill_number=2,
            bill_sum=5,
            bill_date='2022-05-07'
        )
        self.bill1.save()
        response = self.client.get('/bills/')
        self.assertEqual(response.data['bills'],
                         [OrderedDict([
                             ('client_org', 'test_organization_name'),
                             ('bill_number', 2),
                             ('bill_sum', 5),
                             ('bill_date', '2022-05-07')])]
                         )
