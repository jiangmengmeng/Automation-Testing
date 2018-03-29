'''
Created on 2017-1-18

@author: dt198
'''
import time
from selenium.webdriver.common.keys import Keys
from src.commonfunction.CommonFunction import *
from src.commonfunction.ParseXml import *
import unittest

class Dashboard(unittest.TestCase):

    def setUp(self):
        self.commonFunction = CommonFunction()
        self.parseXml = ParseXml()
        self.webdriver = self.commonFunction.start_selenium(self.parseXml.get_msmURL_from_xml())
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_MSM_3(self):
        '''Check if all elements in header bar are displayed correctly'''
        commonFunction = self.commonFunction
        parseXml = self.parseXml
        webdriver =  self.webdriver
        try:
            commonFunction.element_clear(webdriver, parseXml.get_xpath_from_xml("UserNameXpath"))
            commonFunction.send_keys(webdriver,parseXml.get_xpath_from_xml("UserNameXpath"), parseXml.get_account_username_from_xml('SharingAdmin'))
            commonFunction.element_clear(webdriver, parseXml.get_xpath_from_xml("PasswordXpath"))
            commonFunction.send_keys(webdriver,parseXml.get_xpath_from_xml("PasswordXpath"), parseXml.get_account_password_from_xml('SharingAdmin'))
            commonFunction.click(webdriver,parseXml.get_xpath_from_xml("SignInButton"))
        
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@class='leftpanel']/div/h1/a/img[@title='DerbySoft MetaSearch Manager']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@class='headerbar']/div/ul[@class='headermenu']/li/div/button[@id='admin-dropdown']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@class='headerbar']/div/ul[@class='headermenu']/li[2]/div/button[@id='setting-dropdown']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@class='headerbar']/div/ul[@class='headermenu']/li[3]/a/span[@class='icomoon icon-help']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@class='headerbar']/div/ul[@class='headermenu']/li[4]/div/a/span[@class='icomoon icon-bell']"))
        except AssertionError as e:
            self.fail(e)
        except Exception as e:
            self.verificationErrors.append(str(e))
        
    def test_MSM_4(self):
        '''Check if all elements in left panel menu are displayed correctly'''
        commonFunction = self.commonFunction
        parseXml = self.parseXml
        webdriver =  self.webdriver
        try:
            commonFunction.element_clear(webdriver, parseXml.get_xpath_from_xml("UserNameXpath"))
            commonFunction.send_keys(webdriver,parseXml.get_xpath_from_xml("UserNameXpath"), parseXml.get_account_username_from_xml('SharingAdmin'))
            commonFunction.element_clear(webdriver, parseXml.get_xpath_from_xml("PasswordXpath"))
            commonFunction.send_keys(webdriver,parseXml.get_xpath_from_xml("PasswordXpath"), parseXml.get_account_password_from_xml('SharingAdmin'))
            commonFunction.click(webdriver,parseXml.get_xpath_from_xml("SignInButton"))
            time.sleep(2)  #Chrome Webdriver compatibility
            commonFunction.click(webdriver,"//div[@id='msm-menu']/ul/li/a")
            #verify
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@id='msm-menu']/ul/li/a/span[text()='Menu']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@id='msm-menu']/ul/li[2]/a/span[text()='Dashboard']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@id='msm-menu']/ul/li[3]/a/span[text()='Reports']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@id='msm-menu']/ul/li[4]/a/span[text()='Hotels']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@id='msm-menu']/ul/li[5]/a/span[text()='Channels']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@id='msm-menu']/ul/li[6]/a/span[text()='Bidding']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@id='msm-menu']/ul/li[7]/a/span[text()='Alerts']"))
            self.assertTrue(commonFunction.verify_element_at_present(webdriver, "//div[@id='msm-menu']/ul/li[8]/a/span[text()='Management']"))
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
