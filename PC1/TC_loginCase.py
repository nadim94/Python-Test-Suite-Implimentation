import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class LoginTest(unittest.TestCase):

    def login_by_gmail(self):
        print("Login By Gmail")
        self.assertTrue(True)

    def login_by_facebook(self):
        print("Login By facebook")
        self.assertTrue(True)

    def login_by_twitter(self):
        print("Login By Twitter")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
