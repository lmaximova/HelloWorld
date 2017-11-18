from selenium import webdriver


class Google():

    def __init__(self, w_driver):
        self.driver = w_driver
        self.driver.get("http://google.com")
        self.driver.implicitly_wait(5)

    def goToSearchPage(self):
        self.driver.find_element_by_name('q').send_keys("Selenium Testing Tools\n")
        self.driver.implicitly_wait(5)
        numRest = self.driver.find_element_by_id('resultStats').text
        return numRest

    def close(self):
        self.driver.close()
