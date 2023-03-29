import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Pagesobjects.Basic import Basicpage
from Pagesobjects.Searchfile import Searchproduct
from Pagesobjects.listprice import ListPrice


class getPriceTest(unittest.TestCase):

    def setUp(cls):
        cls.driver = webdriver.Chrome(
            service=Service("C:/Users/GaneshDatathreyaManj/Downloads/chromedriver_win32 (1)/chromedriver.exe"))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://ifm.com")
        callingRegion = Basicpage(cls.driver)
        callingRegion.mainFunction()

    def test_display_list_price_ofProduct(self):
        while True:
            searchoption = Searchproduct(self.driver)
            searchoption.inputforSearchText()
            searchoption.verifySameElement()
            listing_the_price = ListPrice(self.driver)
            listing_the_price.list_Price_of_Product()

            search_again = input("Search again? (y/n): ")
            if search_again.lower() != "y":
                break
            else:
                searchoption.clearTheexistingsearch()

        def tearDown(cls):
            cls.driver.quit()

        if __name__ == '__main__':

            unittest.main()

