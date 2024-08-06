import unittest
from app import app

class EssenzStudentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_get_answer(self):
        result = self.app.post('/get_answer', json={'prompt': 'What is AI?'})
        self.assertEqual(result.status_code, 200)
        self.assertIn('answer', result.json)

if __name__ == '__main__':
    unittest.main()
