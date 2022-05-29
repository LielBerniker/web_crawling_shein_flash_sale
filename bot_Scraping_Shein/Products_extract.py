from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bot_Scraping_Shein.Product_Information import Product_information
import time
"""
this class extract two type of web element that may contain an article,
then extract all the links in these elements and return them in list
"""


class Products_extract:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__all_products = []

    def get_all_products(self):
        """
         call functions that extract all type of articles from the web page
         @return: list of all the articles link
         """
        time.sleep(4)
        try:
            self.__driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/i').click()
        except:
            pass
        time.sleep(1)
        try:
            self.__driver.find_element(By.XPATH, '/ html / body / div[8] / div[1] / i').click()
        except:
            pass


        button_flash_sale = self.__driver.find_element(By.CSS_SELECTOR, 'a[data-href-type="flashSale"]')
        button_flash_sale.click()
        # wait until the next button is available
        element1 = WebDriverWait(self.__driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="she-btn-black j-subscribe-submit"]')))
        extract = True
        while extract is True:
            time.sleep(2)
            current_products = self.__driver.find_elements(By.CSS_SELECTOR, 'div[class="S-product-item__name"]')
            for cur_product in current_products:
                self.__get_current_product(cur_product)
            next_btn = self.__driver.find_element(By.CSS_SELECTOR, 'span[aria-label="Page Next"]')
            go_btn = next_btn.get_attribute("aria-disabled")
            if go_btn == "true":
                extract = False
            else:
                next_btn.click()
        return self.__all_products

    def __remove_unnecessary_letters_from_name(self, name):
        """
        fix the article name , by remove all letters that my cause problem in the file create process
        @return:
        """
        article_name = name
        article_name = article_name.replace(':', '')
        article_name = article_name.replace('?', '')
        article_name = article_name.replace('*', '')
        article_name = article_name.replace('<', '')
        article_name = article_name.replace('>', '')
        article_name = article_name.replace('\\', '')
        article_name = article_name.replace('/', '')
        article_name = article_name.replace('|', '')
        article_name = article_name.replace('"', '')
        return article_name

    def __get_current_product(self, current_product: WebElement):
        """
        fix the article name , by remove all letters that my cause problem in the file create process
        @return:
        """

        inner_a = current_product.find_element(By.CSS_SELECTOR, 'a[class^="S-product-item"]')
        self.__get_a_class(inner_a)

    def __get_a_class(self, a_class: WebElement):
        """
        fix the article name , by remove all letters that my cause problem in the file create process
        @return:
        """
        cur_link = a_class.get_attribute("href")
        cur_price = a_class.get_attribute("data-price")
        cur_name = a_class.get_attribute("aria-label")
        cur_name = self.__remove_unnecessary_letters_from_name(cur_name)
        current_product_info = Product_information(cur_name, cur_link, cur_price)
        self.__all_products.append(current_product_info)

