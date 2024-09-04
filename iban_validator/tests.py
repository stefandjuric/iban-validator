from django.test import TestCase
from django.urls import reverse

class IbanValidationTests(TestCase):
    def test_valid_iban(self):
        """Test that a valid Montenegrin IBAN is correctly validated"""
        response = self.client.post(reverse('third_task_view'), {'iban': 'ME25505000012345678951'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['is_valid'], True)

    def test_invalid_iban(self):
        """Test that an invalid Montenegrin IBAN is correctly identified"""
        response = self.client.post(reverse('third_task_view'), {'iban': 'ME25505000012345678900'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['is_valid'], False)

    def test_empty_iban(self):
        """Test that an empty IBAN is handled properly"""
        response = self.client.post(reverse('third_task_view'), {'iban': ''})
        self.assertEqual(response.status_code, 400)

    def test_invalid_request_method(self):
        """Test that GET request is not allowed for the IBAN validation endpoint"""
        response = self.client.get(reverse('third_task_view'))
        print(response.json())
        self.assertEqual(response.status_code, 405)
