from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("https://www.simplyretrofits.com/")
    driver.maximize_window()
    action = ActionChains(driver)
    request.cls.action = action
    request.cls.driver = driver         #driver to be accesible for the class in the baseclass


    yield                       #to be executed at the end of the program
    driver.close()

