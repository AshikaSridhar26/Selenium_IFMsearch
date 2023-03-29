import logging

from selenium.webdriver.common.devtools.v110 import console
from selenium.webdriver.support.wait import WebDriverWait
from logging import exception

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pagesobjects.Searchfile import Searchproduct
import re


class ListPrice:
    wait_time_out = 15
    PriceList = "//span[@class='price-block__listprice__price text-nowrap ng-binding']"
    productsize1 = ".tab-navigation"
    productcount = "//a[@ng-href='#!/product/?_type=product']/span"
    NamefProducts1 = "//a[@class='product-number ng-binding ng-isolate-scope']"
    PriceList2=""

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

    def list_Price_of_Product(self):
        #self.wait_variable.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.productsize1)))
        #self.wait_variable.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.productsize1)))
        flag = self.driver.find_element(By.CSS_SELECTOR, '.tab-navigation').is_displayed()
        if flag:
            productcount = self.driver.find_element(By.XPATH, self.productcount)
            ProductElement = productcount.text
            num = re.findall(r'\d+', ProductElement)
            testdata = int(num[0])

            if testdata>= 1:
                PriceListElements = self.driver.find_elements(By.XPATH, self.PriceList)

                NameofElements1=self.driver.find_elements(By.XPATH, self.NamefProducts1)

                for i in range(0, len(PriceListElements)):
                    print("The list price of the", NameofElements1[i].text, "is:", PriceListElements[i].text)



