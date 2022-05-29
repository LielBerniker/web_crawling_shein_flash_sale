import json

import Constants as Const
import os, shutil

import time

"""
this class extract two type of web element that may contain an article,
then extract all the links in these elements and return them in list
"""


class Save_data_to_files:
    def __init__(self, all_products):
        self.__all_products = all_products
        self.__save_to_json_files()

    def __save_to_json_files(self):
        """
        create a json object to the article and save it in the proper directory
        @return:
        """
        self.__empty_dir()
        time.sleep(0.4)
        for product in self.__all_products:
            product.name = product.name.lower()
            json_obj_style = {
                "name": product.name,
                "price": product.price,
                "link": product.link
            }
            # Serializing json
            json_object = json.dumps(json_obj_style)
            # Writing to sample.json

            file_name = product.name + ".json"
            file_full_path = os.path.abspath(os.getcwd()) + Const.PRODUCTS_PATH + file_name
            with open(file_full_path, "w") as outfile:
                outfile.write(json_object)

    def __empty_dir(self):
        """
         the function delete all files from the directory
         @param path: path to a directory
         @return:
         """
        full_path = os.path.abspath(os.getcwd()) + Const.PRODUCTS_DIR_PATH
        for filename in os.listdir(full_path):
            file_path = os.path.join(full_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
