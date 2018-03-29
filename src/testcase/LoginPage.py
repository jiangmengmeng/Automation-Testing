'''
Created on 2016-12-22

@author: dt198
'''
from selenium.webdriver.common.keys import Keys
from src.commonfunction.CommonFunction import *
from src.commonfunction.ParseXml import *
import unittest

class LoginPage(unittest.TestCase):

    def setUp(self):
        self.commonFunction = CommonFunction()
        self.parseXml = ParseXml()
        self.webdriver = self.commonFunction.start_selenium(self.parseXml.get_msmURL_from_xml())
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_MSM_1(self):
        '''Check if all elements in login page are displayed correctly'''
        commonFunction = self.commonFunction
        parseXml = self.parseXml
        webdriver =  self.webdriver
        try:
            self.assertTrue("Sign In | MetaSearch Manager" in webdriver.title) 
            self.assertTrue(commonFunction.verify_text_at_present(webdriver, "//div[@class='pageheader']", "Please Sign In"))
            self.assertTrue(commonFunction.verify_text_at_present(webdriver, "//div[@class='sign-in-form']/h3", "Enter your user name and password"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@class='logopanel']/h1/a/img[@title='DerbySoft MetaSearch Manager']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//form[@class='form-inline']/div/div/input[@name='username']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//form[@class='form-inline']/div[2]/div/input[@name='password']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@class='form-group remember-me']/label[@data-name='Remember me']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@class='form-group remember-me']/button[contains(text(), 'Sign In')]")) 
        except AssertionError as e:
            self.fail(e)
        except Exception as e:
            self.verificationErrors.append(str(e))
        
    def test_MSM_2(self):   
        '''Check if the sharing admin can login successfully'''
        commonFunction = self.commonFunction 
        parseXml = self.parseXml
        webdriver =  self.webdriver
        try:
            commonFunction.element_clear(webdriver, parseXml.get_xpath_from_xml("UserNameXpath"))
            commonFunction.send_keys(webdriver,parseXml.get_xpath_from_xml("UserNameXpath"), parseXml.get_account_username_from_xml('SharingAdmin'))
            commonFunction.element_clear(webdriver, parseXml.get_xpath_from_xml("PasswordXpath"))
            commonFunction.send_keys(webdriver,parseXml.get_xpath_from_xml("PasswordXpath"), parseXml.get_account_password_from_xml('SharingAdmin'))
            commonFunction.click(webdriver,parseXml.get_xpath_from_xml("SignInButton"))
            self.assertTrue("Dashboard | MetaSearch Manager" in webdriver.title)
        except AssertionError as e:
            self.fail(e)
        except Exception as e:
            self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.webdriver.close()
        self.webdriver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == '__main__': 
    unittest.main()       

