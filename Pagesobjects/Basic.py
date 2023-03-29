from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basicpage:
    wait_time_out = 5
    regionandlanguage = "//a[@href='/de/de']"
    aceeptCookie = ".uc-btn-accept-wrapper #uc-btn-accept-banner"

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

    def mainFunction(self):
        self.wait_variable.until(EC.element_to_be_clickable((By.XPATH, self.regionandlanguage))).click()
        self.wait_variable.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.aceeptCookie))).click()
