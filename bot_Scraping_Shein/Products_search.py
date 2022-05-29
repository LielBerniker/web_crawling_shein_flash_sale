import os
import json
import glob
from prettytable import PrettyTable
import Constants as Const

"""
this class collect all the flights that contain the words the user inserted,
then print the information of the flights bt the table match to the flight type , arrival or departure
"""


class Products_search():
    def __init__(self,search_list):
        self.__text_words = search_list
        self.__products = []
        self.__search_products()

    def __search_products(self):
        """
        call functions that search in the json files for the flights that contain the text'
        then print the flights in tables
        @return:
        """
        self.__get_all_products()
        self.__show_products_in_table()

    def __get_all_products(self):
        """
         go over all the json files in the flight arrival directory
         then get information only from the ones that contains some of the search text in one of their attributes
         @return:
         """
        path = os.path.abspath(os.getcwd()) + Const.PRODUCTS_DIR_PATH
        for filename in glob.glob(os.path.join(path, '*.json')):  # only process .JSON files in folder.
            with open(filename, encoding='utf-8', mode='r') as currentFile:
                json_data = json.loads(currentFile.read())
                # get all the flight information
                product_info = [json_data["name"], json_data["price"], json_data["link"]]
                cur_name = json_data["name"]
                if self.__product_text_check(cur_name):
                    self.__products.append(product_info)

    def __product_text_check(self, cur_name):
        """
        checks if the currnt contain any word from the search text in one of his attributes
        @param cur_flight: current flight information
        @return: True one of the flight fields contain one of the text word, False o.w.
        """
        for word in self.__text_words:
            if word in cur_name:
                return True
        return False

    def __show_products_in_table(self):
        """
        print all the arrival flight that match the conditions in a table
        @return:
        """
        table = PrettyTable(
            field_names=["         name          ", " price ", "           link           ",
                         ])
        table.title = "ALL PRODUCTS"
        table.add_rows(self.__products)
        print(table)

