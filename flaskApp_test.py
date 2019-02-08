from flaskApp import app

import unittest
import json

# I understand that these aren't thorough tests
class JokesTestCase(unittest.TestCase):

  # dad joke route
  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/dadjoke', content_type='text/plain')
    self.assertEqual(response.status_code, 200)

  # advice route
  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/advice', content_type='application/json')
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()