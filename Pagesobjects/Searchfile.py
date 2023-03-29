import logging
from logging import exception

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Searchproduct:
    wait_time_out = 5

    search_button = "button[class='ifm-search-bar__submit normalize ifm-button']"
    search_item = ".ifm-search-bar__input-wrapper #search-bar__input"
    Name_of_product = ".product-number.ng-binding.ng-isolate-scope"
    Search_close_button = "//*[name()='use' and contains(@href,'#close-cir')]"
    ProductName = ""
    User_input = ""
    ProductNameInAnotherPage = ""

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

    def inputforSearchText(self):
        input_searchbox: WebElement = self.wait_variable.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.search_item)))
        self.User_input = input("Please enter the desired item designation:")
        input_searchbox.send_keys(self.User_input)
        print(self.User_input)
        try:
            if self.driver.find_element(By.XPATH, self.Search_close_button).is_displayed():
                self.driver.find_element(By.CSS_SELECTOR, self.search_button).click()
            else:
                raise exception("Please fill the mandatory field")
        except Exception as e:
            print(e)

    def verifySameElement(self):

        if self.driver.find_element(By.CSS_SELECTOR, '.infobox__text').is_displayed():
            print("Product is not found")
            self.ProductName = self.driver.find_element(By.CSS_SELECTOR, '#searchInfoNoResults').text

        else:
            Product_Description: WebElement = self.driver.find_element(By.CSS_SELECTOR, self.Name_of_product)

            self.ProductName = Product_Description.text

    def clearTheexistingsearch(self):
        self.driver.find_element(By.XPATH, self.Search_close_button).click()

    def SearchthroughDropdown(self):
        input_searchbox: WebElement = self.wait_variable.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.search_item)))
        self.User_input = input("Please enter the desired item designation:")
        input_searchbox.send_keys(self.User_input)
        print(self.User_input)
        self.driver.find_element(By.XPATH,
                                 "//*[@class='ifm-search-overlay__section']/div/following-sibling::a[contains(@href," + self.User_input.upper() + ")]").click()
        Product_Description2: WebElement = self.driver.find_element(By.CSS_SELECTOR, '.product-header__article')
        self.ProductNameInAnotherPage = Product_Description2.text
