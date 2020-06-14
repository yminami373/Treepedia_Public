import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import unittest
from Treepedia import GreenView_Calculate

class TestGreenViewCalculate(unittest.TestCase):
    def test_get_api_url(self):
        panoID = "0TZEoCxMscKUg5y7BpADBQ"
        heading = 0
        pitch = 0
        key = "MyKey"
        actual_url = GreenView_Calculate.get_api_url(panoID, heading, pitch, key)
        expected_url = "http://maps.googleapis.com/maps/api/streetview?size=400x400&pano=0TZEoCxMscKUg5y7BpADBQ&fov=60&heading=0&pitch=0&sensor=false&key=MyKey&source=outdoor"

        self.assertEqual(actual_url, expected_url)


if __name__ == '__main__':
    unittest.main()