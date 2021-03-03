from django.test import TestCase, Client
from django.contrib.auth.models import User


class ApiFixture(TestCase):
    """
    call this function before every test case
    """
    def setUp(self):
        User.objects.create_user(username='test_user', email=None, password='Ipgeolocation_Zadanie')
        pass

    def test_get_on_root_returs_success(self):
        c = Client()
        self.assertEqual(200, c.get("/").status_code)
        self.assertEqual({"hello": "world"}, c.get("/test_mat").json())

    def test_get_access_token(self):
        c = Client()
        response = c.post('/api/token', {'username': 'test_user', 'password': 'Ipgeolocation_Zadanie'})
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json()["access"]) > 0)

        response2 = c.post('/api/token', {'username': 'test_user', 'password': 'Ipgeolocation_Zadanie'})
        self.assertNotEqual(response2.json()["access"], response.json()["access"])

