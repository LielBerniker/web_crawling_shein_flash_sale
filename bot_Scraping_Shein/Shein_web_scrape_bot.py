from Web_scrape_bot import Web_scrape_bot
import Constants as Const
from bot_Scraping_Shein.Products_extract import Products_extract
from bot_Scraping_Shein.Save_data_to_files import Save_data_to_files
from bot_Scraping_Shein.Products_search import Products_search
"""
this class represent a bot that extracts all the news links in the bbc main page
"""


class Shein_web_scrape_bot():
    def __init__(self, driver_path=Const.DRIVER_PATH):
        self.__driver = Web_scrape_bot(driver_path)
        self.__products_list = []
        self.update_products_storage()

    def update_products_storage(self):
        """
        this function first extract all the links of potential articles from the bbx web page
        then go over each link and extract the article content and name from it
        finally save it to a json , only if the article didn't already exist
        @return:
        """
        self.__driver.determine_page(Const.SHEIN_URL)
        all_products = Products_extract(self.__driver)
        self.__products_list = all_products.get_all_products()
        Save_data_to_files(self.__products_list)

    def search_in_articles(self, search_text):
        """
        the function go over all the content of the articles
        then print the name and link of all articles that contain attlist half of the words in search
        @param self: string that contain words
        @return:
        """
        self.update_products_storage()
        text_lower = search_text.lower()
        text_list = list(text_lower.split(" "))
        Products_search(text_list)
