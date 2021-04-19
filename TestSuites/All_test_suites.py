import unittest
from Package2.TC_paymentCase import PaymentTest
from Package2.TC_paymentreturnCase import PaymentReturnbyBankTest

from PC1.TC_loginCase import LoginTest
from PC1.TC_signupCase import SignupTest

# All Test Case Loader
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnbyBankTest)

# Creating Test Suite
login_signup_test_suite = unittest.TestSuite([tc1, tc2])
payment_test_suite = unittest.TestSuite([tc3, tc4])
master_test_suite = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner().run(login_signup_test_suite)
