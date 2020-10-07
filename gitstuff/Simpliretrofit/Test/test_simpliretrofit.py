import time

from selenium.webdriver.support.select import Select
from PageObjects.HomePage import HomePage
from BaseClass.Baseclass import BaseClass
from PageObjects.Products import Products
from PageObjects.product import Product
from PageObjects.waitelements import wait_element


class TestSimply(BaseClass):

    def test_homepage(self):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        product = Product(self.driver)
        wait_ele = wait_element(self.driver)
        Element_list = Products(self.driver, self.action)
        self.search_item().click()
        log.info('Entering LED string')
        self.search_item().send_keys('LED')
        log.info('waiting to appear the search suggestions')
        wait_ele.waitforsearchelement()
        suggestions = self.Search_Suggestions()
        for suggest in suggestions:
            print(suggest.text)
            if "140w 347v" in suggest.text:
                suggest.click()
                break

        log.info('setting the color temp from the options')
        sel = Select(product.color_temp())
        sel.select_by_visible_text('4000K')
        product.add_to_cart().click()
        wait_ele.waitforproduct()
        log.info('click on the commercial tag')

        Element_list.Product_list()
        time.sleep(5)
        self.search_item().send_keys('wrap')
        log.info('entering wrap into search option')
        wait_ele.waitforsearchelement()
        suggests_commercial = self.Search_Suggestions()

        for suggest_commercial in suggests_commercial:
            print(suggest_commercial.text)
            if "Linkable Wrap Light 48w" in suggest_commercial.text:
                suggest_commercial.click()
                break
        time.sleep(3)
        sel = Select(product.color_temp())
        sel.select_by_visible_text('4000K')
        product.add_to_cart().click()
        log.info('Added commercial light to the cart')
        homepage.shop_item().click()
        time.sleep(5)
        Element_list.Decorative_list()


