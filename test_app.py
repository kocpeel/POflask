import unittest
from flask_testing import TestCase
from main import app, users


def create_app(self):
    app.config['TESTING'] = True
    return app

def test_get_users(self):
    response = self.client.get('/users')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, users)



if __name__ == '__main__':
   unittest.main()