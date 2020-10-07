from selenium.webdriver.common.by import By
from PageObjects.waitelements import wait_element


class Products:
    Productlist = (By.XPATH, "//li[@id = 'menu-item-17810']/a")  # class variable
    commercial = (By.ID, "menu-item-18227")  # class variable
    Decorative = (By.ID, "menu-item-18226")  # decorative tab
    filamentlamp = (By.ID, "menu-item-18232")  # filament lamp under decoratve tab

    def __init__(self, driver, action):  # constructor
        self.driver = driver
        self.action = action

    def Product_list(self):
        wait = wait_element(self.driver)
        self.action.move_to_element(self.driver.find_element(*Products.Productlist)).perform()  # move the cursor to product
        wait.waitforproduct()
        self.action.move_to_element(self.driver.find_element(*Products.commercial)).click().perform()  # move and click at commerical tag

    def Decorative_list(self):
        self.action.move_to_element(self.driver.find_element(*Products.Productlist)).perform()  # move the cursor to product
        self.action.move_to_element(self.driver.find_element(*Products.Decorative)).perform()
        wait = wait_element(self.driver)
        wait.wait_for_decorative_elements()
        self.action.move_to_element(self.driver.find_element(*Products.filamentlamp)).click().perform()

