from selenium import webdriver

class GoogleSearchPage():
    def __init__(self, w_driver):
        self.driver = webdriver
        print(self.driver.title)

    def getNumberofResults(self):
        numberofResults = self.driver.find_element_by_id('resultsStats').wrapped_element.text
        return numberofResults

    def getTitle(self):
        return self.driver.title