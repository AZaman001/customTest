from flaskTest import app

import unittest
import json

class JokesTestCase(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/dadjokes', content_type='text/plain')
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()