from selenium.webdriver.common.by import By


class HomePage:
    shop = (By.CSS_SELECTOR,"li[id = 'menu-item-15369']")   #shop button
    homelogo = (By.ID, "logo")
    def __init__(self,driver):
        self.driver = driver

    def shop_item(self):
        return self.driver.find_element(*HomePage.shop)           #calling shop button

    def home_logo(self):
        return self.driver.find_element(*HomePage.homelogo)


