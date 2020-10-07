from selenium.webdriver.common.by import By


class Product:
    Colortemp = (By.CSS_SELECTOR, "select[id = 'pa_color-temperature']")    #select color temperature static dropdown
    addcart = (By.CSS_SELECTOR, "button[type = 'submit']")              #add to cart button

    def __init__(self, driver):
        self.driver = driver

    def color_temp(self):
        return self.driver.find_element(*Product.Colortemp)       #calling color temp selection

    def add_to_cart(self):
        return self.driver.find_element(*Product.addcart)       #calling add to cart button
