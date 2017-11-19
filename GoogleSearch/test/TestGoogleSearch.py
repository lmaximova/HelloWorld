import unittest

from GoogleSearch.main_source.Google import Google
from selenium import webdriver

class MyTestCaseTest(unittest.TestCase):

    def setUp(self):
        self.googlePage = Google(webdriver.Chrome())


    def tearDown(self):
        self.googlePage.close()

    def test_googleSearch(self):
        googleSearch = self.googlePage.goToSearchPage()
        assert googleSearch != '0'

    def test_googleTitle(self):
        title = self.googlePage.getTite()
        assert title == 'Google', 'Wrong page title'


if __name__ == '__main__':
    unittest.main()
