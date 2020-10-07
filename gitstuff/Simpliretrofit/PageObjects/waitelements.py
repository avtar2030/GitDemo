from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class wait_element:

    def __init__(self,driver):
        self.driver = driver


    def waitforsearchelement(self):                 #wait to display search elements on the website
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[class = 'aws_result_title']")))

    def waitforproduct(self):                #wait to appear product tag on the website
        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.element_to_be_clickable((By.ID, 'menu-item-17810')))

    def wait_for_decorative_elements(self):
        wait = WebDriverWait(self.driver,4)
        wait.until(EC.element_to_be_clickable((By.ID,'menu-item-18232')))



