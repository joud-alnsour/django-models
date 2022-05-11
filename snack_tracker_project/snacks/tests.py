from django.test import TestCase
from django.urls import reverse 

class SnackTest(TestCase):
    def test_snack_list_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'snack_list.html')

    def test_snack_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_list.html')
        self.assertTemplateUsed(response,'base.html')