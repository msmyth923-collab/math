import unittest
from sub_app import app

class TestSubtractor(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_subtract_valid_numbers(self):
        response = self.app.get('/subtract?a=10&b=4')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['a'], 10.0)
        self.assertEqual(data['b'], 4.0)
        self.assertEqual(data['result'], 6.0)

    def test_get_subtract_floats(self):
        response = self.app.get('/subtract?a=5.5&b=2.2')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertAlmostEqual(data['result'], 3.3, places=6)

    def test_get_subtract_missing_params(self):
        response = self.app.get('/subtract?a=5')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_get_subtract_invalid_params(self):
        response = self.app.get('/subtract?a=foo&b=3')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_post_subtract_valid_json(self):
        response = self.app.post('/subtract', json={'a': 10, 'b': 4})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['result'], 6.0)

    def test_post_subtract_missing_body(self):
        response = self.app.post('/subtract')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_post_subtract_invalid_json(self):
        response = self.app.post('/subtract', json={'a': 'x', 'b': 3})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Subtractor Service')
        self.assertIn('usage', data)

if __name__ == '__main__':
    unittest.main()