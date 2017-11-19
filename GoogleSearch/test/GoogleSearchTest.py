import unittest

from GoogleSearch.main_source.Google import Google
from selenium import webdriver

class MyTestCaseTest(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome("C:\\Selenium\\Chrome\\chromedriver_win32\chromedriver.exe")
        self.googlePage = Google(webdriver.Chrome("C:\\Selenium\\Chrome\\chromedriver_win32\chromedriver.exe"))


    def tearDown(self):
        self.googlePage.close()

    def test_googleSearch(self):
        googleSearch = self.googlePage.goToSearchPage()
        assert googleSearch != '0'




if __name__ == '__main__':
    unittest.main()
