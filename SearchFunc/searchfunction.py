import logging
import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Pagesobjects.Basic import Basicpage
from Pagesobjects.Searchfile import Searchproduct


class SearchFunctionTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(
            service=Service("C:/Users/GaneshDatathreyaManj/Downloads/chromedriver_win32 (1)/chromedriver.exe"))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://ifm.com")
        callingRegion = Basicpage(cls.driver)
        callingRegion.mainFunction()

    def test_verify_search_text(self):
        searchoption = Searchproduct(self.driver)
        searchoption.inputforSearchText()
        searchoption.verifySameElement()
        self.assertEqual(searchoption.User_input.upper(), searchoption.ProductName)

    def test_searchhroughDropDown(self):
        searchoption = Searchproduct(self.driver)
        searchoption.SearchthroughDropdown()
        logging.info(self.assertEqual(searchoption.User_input.upper(), searchoption.ProductNameInAnotherPage))

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    if __name__ == '__main__':


        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)7s:%(message)s')
        logging.info("start")

        logging.info("end")
        unittest.main()
