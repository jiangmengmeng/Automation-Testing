'''
Created on 2017-1-18

@author: dt198
'''
import os
from LoginPage import *
from Dashboard import *
from src.lib.HTMLTestRunner import *

if __name__ == '__main__':    
    report_title = u'MetaSearch Manager Automation Testing Result'
    desc = u'Regression Testing Result'
    project_path=os.path.dirname(os.getcwd())
    report_file = project_path + '\\testreport\\MSMAutomationTestingResult' + time.strftime("%Y%m%d%H", time.localtime()) + '.html'
    
    testsuite1 = unittest.TestLoader().loadTestsFromTestCase(LoginPage)
    testsuite2 = unittest.TestLoader().loadTestsFromTestCase(Dashboard)
    testsuite = unittest.TestSuite([testsuite1, testsuite2]) 

    fp=file(report_file,"wb") 
    runner = HTMLTestRunner(stream=fp, title=report_title, description=desc)
    runner.run(testsuite)
    fp.close()