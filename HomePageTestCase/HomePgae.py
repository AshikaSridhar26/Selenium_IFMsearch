import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Pagesobjects.Basic import Basicpage
from Pagesobjects.Searchfile import Searchproduct


class HomePageTest(unittest.TestCase):

    def setUp(cls):
        cls.driver = webdriver.Chrome(
            service=Service("C:/Users/GaneshDatathreyaManj/Downloads/chromedriver_win32 (1)/chromedriver.exe"))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://ifm.com")
        callingRegion = Basicpage(cls.driver)
        callingRegion.mainFunction()

    def test_search_box(self):
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, Searchproduct.search_item))

    def tearDown(cls):
        cls.driver.quit()

        def is_element_present(self, how, what):

            try:
                self.driver.find_element(by=how, value=what)
            except NoSuchElementException:
                return False
            return True

    if __name__ == '__main__':
        unittest.main()


