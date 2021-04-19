import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class SignupTest(unittest.TestCase):

    def signup_by_gmail(self):
        print("signup By Gmail")
        self.assertTrue(True)

    def signup_by_facebook(self):
        print("signup By facebook")
        self.assertTrue(True)

    def signup_by_twitter(self):
        print("signup By Twitter")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
