'''
Created on 2017-1-12

@author: dt198
'''
from xml.etree import ElementTree

class ParseXml:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def get_account_username_from_xml(self, accountName):
        allAccounts = ElementTree.parse('../commondata/TestAccount.xml').getroot()
        path = ".//*[@name='" + accountName + "']/username"
        return allAccounts.findtext(path)
    
    def get_account_password_from_xml(self, accountName):
        allAccounts = ElementTree.parse('../commondata/TestAccount.xml').getroot()
        path = ".//*[@name='" + accountName + "']/password"
        return allAccounts.findtext(path)
        
    def get_xpath_from_xml(self, nodeName):
        allXpath = ElementTree.parse('../commondata/CommonXpath.xml').getroot()
        return allXpath.findtext(nodeName)
    
    def get_msmURL_from_xml(self):
        allXpath = ElementTree.parse('../commondata/CommonXpath.xml').getroot()
        return allXpath.get('serverPath')
    
    