'''
Created on 2016-12-22

@author: dt198
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By
import traceback
from selenium.common.exceptions import NoSuchElementException

class CommonFunction:
    '''
    classdocs
    '''
    def __init__(self):
        '''
         description
        '''
            
    def start_selenium(self, url):
        driver = webdriver.Chrome("..\lib\chromedriver.exe")
        driver.get(url)
        return driver
    
    def close_selenium(self, driver):
        driver.close()
        driver.quit()
        
    def find_element_by_name(self, driver, elementName):
        elem = driver.find_element_by_name(elementName)
        return elem
    
    def find_element_by_id(self, driver, elementId):
        elem = driver.find_element_by_id(elementId)
        return elem
    
    def find_element_by_xpath(self, driver, xpath):
        elem = driver.find_element_by_xpath(xpath)
        return elem
    
    def find_element_by_tag_name(self, driver, elementTagName):
        elem = driver.find_element_by_tag_name(elementTagName)
        return elem
    
    def find_elements_by_css_selector(self, driver, cssSelector):
        elem = driver.find_elements_by_css_selector(cssSelector)
        return elem  
        
    def switch_to_window(self, driver, windowName):
        driver.switch_to_window(windowName)
        
    def switch_to_frame(self, driver, frameName):
        driver.switch_to_frame(frameName)
        driver.switch_to_frame(1)
    
    def switch_to_alert(self, driver):
        driver.switch_to_alert()
    
    def element_clear(self, driver, xpath):
        driver.find_element_by_xpath(xpath).clear()
    
    def send_keys(self, driver, xpath, keyValue):
         driver.find_element_by_xpath(xpath).send_keys(keyValue)  
        
    def click(self, driver, xpath): 
        locator = (By.XPATH, xpath)
        WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located(locator), "The element('" + xpath + "')can't be found!")  
        driver.find_element_by_xpath(xpath).click()     
        
    def page_forward(self, driver):
        driver.forward() 
    
    def page_back(self, driver):
        driver.back() 
        
    def verify_text_at_present(self, driver, xpath, text):
        try:
            if driver.find_element_by_xpath(xpath).text == text:
                return True
            else:
                print "The xpath",xpath,"can't be found!" 
                return False
        except NoSuchElementException as e: 
            print 'Exception:',e
            return False
    
    def verify_element_at_present(self, driver, xpath):
        try:
            if driver.find_element_by_xpath(xpath) != "":
                return True
            else:
                print "The xpath",xpath,"can't be found!" 
                return False
        except NoSuchElementException as e: 
            print 'Exception:',e
            return False  
