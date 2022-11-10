#!/home/python/venv/main/bin/python

import sys
sys.path.append("..")
import unittest
from src import main

class MainTest(unittest.TestCase):
  def test_main(self):
    response = main.main()
    expected = "Hey there"
    self.assertEqual(expected, response)

if __name__ == "__main__":
  unittest.main()
