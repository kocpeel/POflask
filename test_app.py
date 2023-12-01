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

def test_get_user(self):
    response = self.client.get('/users/1')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, users[0])

def test_create_user(self):
    response = self.client.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.json, users[-1])

def test_update_user(self):
    response = self.client.patch('/users/1', json={"name": "Jan"})
    self.assertEqual(response.status_code, 204)
    self.assertEqual(users[0]['name'], "Jan")

def test_replace_user(self):
    response = self.client.put('/users/1', json={"name": "Jan", "lastname": "Kowalski"})
    self.assertEqual(response.status_code, 204)
    self.assertEqual(users[0], {"id": 1, "name": "Jan", "lastname": "Kowalski"})

def test_delete_user(self):
    response = self.client.delete('/users/1')
    self.assertEqual(response.status_code, 204)
    self.assertEqual(len(users), 0)

if __name__ == '__main__':
   unittest.main()