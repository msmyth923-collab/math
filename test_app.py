import unittest
from app import app  # Import your Flask app

class TestAdder(unittest.TestCase):
    def setUp(self):
        """Set up the test client before each test."""
        self.app = app.test_client()
        self.app.testing = True  # Enable testing mode for better error handling

    def test_get_add_valid_numbers(self):
        """Test GET /add with valid numeric query parameters."""
        response = self.app.get('/add?a=5&b=3')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['a'], 5.0)
        self.assertEqual(data['b'], 3.0)
        self.assertEqual(data['result'], 8.0)

    def test_get_add_floats(self):
        """Test GET /add with floating-point numbers."""
        response = self.app.get('/add?a=5.5&b=2.5')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['result'], 8.0)

    def test_get_add_negative_numbers(self):
        """Test GET /add with negative numbers."""
        response = self.app.get('/add?a=-5&b=3')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['result'], -2.0)

    def test_get_add_missing_parameters(self):
        """Test GET /add with missing parameters."""
        response = self.app.get('/add?a=5')  # Missing 'b'
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

    def test_get_add_invalid_parameters(self):
        """Test GET /add with non-numeric parameters."""
        response = self.app.get('/add?a=abc&b=3')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

    def test_post_add_valid_json(self):
        """Test POST /add with valid JSON body."""
        response = self.app.post('/add', json={'a': 5, 'b': 3})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['a'], 5.0)
        self.assertEqual(data['b'], 3.0)
        self.assertEqual(data['result'], 8.0)

    def test_post_add_floats(self):
        """Test POST /add with floating-point JSON."""
        response = self.app.post('/add', json={'a': 5.5, 'b': 2.5})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['result'], 8.0)

    def test_post_add_negative_numbers(self):
        """Test POST /add with negative numbers in JSON."""
        response = self.app.post('/add', json={'a': -5, 'b': 3})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['result'], -2.0)

    def test_post_add_missing_fields(self):
        """Test POST /add with missing JSON fields."""
        response = self.app.post('/add', json={'a': 5})  # Missing 'b'
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

    def test_post_add_invalid_json(self):
        """Test POST /add with non-numeric JSON values."""
        response = self.app.post('/add', json={'a': 'abc', 'b': 3})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

    def test_post_add_no_json(self):
        """Test POST /add without JSON body."""
        response = self.app.post('/add')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

    def test_home_route(self):
        """Test GET / for the home route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Adder Service')
        self.assertIn('usage', data)

if __name__ == '__main__':
    unittest.main()