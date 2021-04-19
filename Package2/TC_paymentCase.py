import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class PaymentTest(unittest.TestCase):

    def payment_by_dollar(self):
        print("payment By Dollar")
        self.assertTrue(True)

    def payment_by_rupee(self):
        print("payment By rupee")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
