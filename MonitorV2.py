import json
import random
import sys
import threading
import time
import webbrowser
import winsound
from datetime import datetime
from random import seed
import requests
from helper_classes.MobileStock import MobileStock
from helper_classes.Style import Style

__author__ = "Andrew Galvin"
__copyright__ = "Copyright 2020, Andrew Galvin"
__version__ = "0.1.2"
__maintainer__ = "Andrew Galvin"
__status__ = "Alpha"


def sheetGreen():
    return """
            QLabel {
                background-color: #3A506B;
                color: #CAF0F8;
                border: 3px solid green;
                border-radius: 5px;
                font-weight: bold;
            }
            QLabel::hover {
                background-color: #1C2541;
                border: 3px solid green;
            }
            QLabel:pressed {
                background-color: #0B132B;
            }
            """


def sheetRed():
    return """
            QLabel {
                background-color: #3A506B;
                color: #CAF0F8;
                border: 3px solid red;
                border-radius: 5px;
                font-weight: bold;
            }
            QLabel::hover {
                background-color: #1C2541;
                border: 3px solid red;
            }
            QLabel:pressed {
                background-color: #0B132B;
            }
            """


def start_browser(path, url):
    """
    Method to open a given URL in the user's Chrome Browser
    @param path: User's chrome.exe path
    @param url: URL to open in Chrome
    """
    webbrowser.open(url)


# def start_browser_automated(url):
#
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
#     driver = webdriver.Chrome()
#     driver.get(url)
#     driver.find_element_by_name("order[billing_name]").send_keys("Test Test")
#     driver.find_element_by_name("order[email]").send_keys("test@gmail.com")
#     driver.find_element_by_name("order[tel]").send_keys("1234567891")
#     driver.find_element_by_name("order[billing_address]").send_keys("123 Test St")
#     driver.find_element_by_name("order[billing_zip]").send_keys("22222")
#     driver.find_element_by_name("order[billing_city]").send_keys("New York City")
#     Select(driver.find_element_by_name("order[billing_state]")).select_by_visible_text("NY")
#     driver.find_element_by_xpath("//input[@placeholder='number']").send_keys("12334567890")
#     driver.find_element_by_xpath("//input[@placeholder='CVV']").send_keys("123")
#     Select(driver.find_element_by_name("credit_card[month]")).select_by_visible_text("12")
#     Select(driver.find_element_by_name("credit_card[year]")).select_by_visible_text("2020")
#     driver.find_element_by_name("commit").click()


def exists_in_list(sty, product_list):
    """
    Method to check if a given product style is in a given product list
    @param sty: Specific product style
    @param product_list: List of all products and their styles
    @return: True/False dependent on if the item is in the list,
             location of the product in the list, and if the item
             has been added before
    """
    list_count = 0
    for p in product_list:
        if sty.name == p.name and sty.color == p.color:
            if sty.size == p.size:
                return True, list_count, p.added
        list_count += 1
    return False, list_count, False


def get_new_url(product_id):
    """
    Method to generate the URL which contains the product information
    @param product_id: The product's given ID for all styles of that product
    @return: The URL for the specific product
    """
    return "https://www.supremenewyork.com/shop/{0}{1}".format(product_id, ".json")


def get_mobile_data(s, mobile_headers):
    """
    Method to get the data regarding product stock from Supreme
    @param s: requests.Session()
    @param mobile_headers: Mobile header parameters for requests.Session().get()
    @return: The product stock data
    """
    return s.get(url="https://www.supremenewyork.com/mobile_stock.json", headers=mobile_headers)


def get_desktop_data(s, url, desktop_headers):
    """
    Method to get the data which contains the stock information for a specific product style
    @param s: requests.Session()
    @param url: Specific product style.json URL
    @param desktop_headers: Desktop header parameters for requests.Session().get()
    @return: The specific product style data
    """
    return s.get(url=url, headers=desktop_headers)


def get_chrome_user_agent():
    """
    Method to choose a random Chrome User Agent from a file
    @return: Random Chrome User Agent
    """
    with open('chrome_user_agents.txt', 'r') as f:
        return f.readlines()


def print_item_restocked(style_name, style_color, time_now, links):
    """
    Method to print to the user the information regarding an item that has restocked
    @param style_name: Product name
    @param style_color: Product Color
    @param time_now: Time the item restocked
    @param links: The links for each size to add the item to cart
    """
    restocked = "[RESTOCK] {0} [{1}] has restocked at {2}.\n".format(str(style_name),
                                                                     str(style_color),
                                                                     time_now.strftime(
                                                                         "%H:%M:%S"))
    atc_link = "[RESTOCK] Add to cart link: \n"
    for sz, lnk in links.items():
        atc_link += "[RESTOCK] " + sz + ": " + lnk
    print(restocked)
    print(atc_link)


# def print_item_sold_out(style_name, style_color, style_size, time_now):
#     """
#     Method to print to the user that an item has sold out.
#     @param style_name: Product name
#     @param style_color: Product color
#     @param style_size: Product Size
#     @param time_now: Time the item sold out
#     """
#     print(
#         "[SOLD OUT] {0} [{1}] in [{2}] has sold out at {3}.\n".format(
#             str(style_name),
#             str(style_color),
#             str(style_size),
#             time_now.strftime(
#                 "%H:%M:%S")))


def start_open_link(check_time, start_time, chrome_path, link, item_name):
    """
    Method to open the add to cart link in browser if the item is found and in stock
    @param check_time: Time the item was found
    @param start_time: Time the search started
    @param chrome_path: Path to the user's chrome.exe
    @param link: Product add to cart link
    @param item_name: Product name
    """
    try:
        print("[Status] Adding to cart...\n[TOTAL TIME] {:5.3f}".format(
            check_time - start_time) + " seconds" + "\nStarted -> {0}\n   Ended -> {1}".format(
            datetime.fromtimestamp(start_time).strftime("%I:%M:%S"),
            datetime.fromtimestamp(check_time).strftime("%I:%M:%S")))
        browser_thread = threading.Thread(target=start_browser,
                                          args=(chrome_path, link))
        browser_thread.start()
        print("[Status] Task {0} has stopped...".format(str(item_name)))
    except Exception as e:
        print("Error")
        print(e)


user_agents = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
               'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
               'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
               'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36']


class Monitor:
    """
    Class which deals with monitoring Supreme's site to either:
        Add the product to cart
        Monitor all products for restocks
        Monitor an individual product for restocks

    To be used with Gui.py
    """
    mobile_headers = {
        'authority': 'www.supremenewyork.com',
        'method': 'GET',
        'path': '/mobile_stock.json',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflat, br',
        'accept-language': 'en-US,en;q=0.9',
        'upgrade-insecure-requests': '1',
        'Cache-Control': 'max-age=0',
    }
    desktop_headers = {
        'authority': 'www.supremenewyork.com',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'upgrade-insecure-requests': '1',
        'Cache-Control': 'max-age=0',
    }

    # chrome_path = "open -a /Applications/Google\ Chrome.app %s"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    all_products = []

    def start_search2(self, input_name, input_size, input_color, product_list, label):
        """
        Method to search Supreme's site and open the item in Supreme's "Checkout" page
        if the item is found and in stock.

        @param input_name: Product name
        @param input_size: Product size
        @param input_color: Product color
        @param product_list: Empty list to be filled with all products on Supreme's "new" category
        """
        if input_name != "" and input_color != "":
            print("\n[Status] Task {3} starting...\n[Status] Looking for -> [{2}] [{0}] [{1}]\n".format(input_name,
                                                                                                        input_size,
                                                                                                        input_color,
                                                                                                        input_name))
            label.setText("Starting...")
            try:
                added = True
                # While loop to continue until the item is opened in the user's Chrome browser
                while added:
                    label.setText("Searching for product...")

                    # Set seed for the random to be different each iteration
                    seed(1)
                    # Set user-agent headers
                    agent = random.choice(user_agents)
                    self.desktop_headers['user-agent'] = agent[2:len(agent) - 3]
                    self.mobile_headers['user-agent'] = agent[2:len(agent) - 3]

                    # Set start time
                    start_time = time.time()
                    with requests.Session() as s:
                        data = json.loads(get_mobile_data(s, self.mobile_headers).text)

                        # Get all the products on /mobile_stock.json and add them to a list
                        mobile_products = []
                        for category, products in data['products_and_categories'].items():
                            if category == 'new' or category == 'Shoes':
                                for product in products:
                                    if product['name'].lower().__contains__(input_name.lower()):
                                        category_name = product['category_name']
                                        name = product['name']
                                        product_id = product['id']
                                        new_item = product['new_item']
                                        price = product['price']
                                        label.setText("Product found!")
                                        mobile_product = MobileStock(category_name=category_name, name=name,
                                                                     id=product_id,
                                                                     new_item=new_item,
                                                                     price=price)
                                        mobile_products.append(mobile_product)

                        # Search through all /product_id.json
                        for product in mobile_products:
                            data = json.loads(get_desktop_data(s, get_new_url(product.id), self.desktop_headers).text)

                            all_size_options = {}
                            item_name = product.name
                            atc_value = product.id

                            # Search through all product styles
                            for item in data['styles']:
                                # Search through all product sizes and checks stock level for each size
                                for size in item['sizes']:

                                    color = item['name']
                                    color_id = item['id']

                                    size_name = size['name']
                                    size_id = size['id']
                                    stock_level = size['stock_level']

                                    all_size_options[size_name] = [size_id, stock_level]
                                    style = Style(name=item_name, color=color, color_id=color_id, size=size_name,
                                                  size_id=size_id,
                                                  stock_level=stock_level, atc_value=atc_value,
                                                  all_sizes=all_size_options)

                                    result = exists_in_list(style, product_list)
                                    style_index = result[1]
                                    # If the item is in the list
                                    if result[0]:
                                        style.setAdded(result[2])
                                        old_stock_level = product_list[style_index].stock_level
                                        # If the item is in stock and the link has not opened yet, open it
                                        if stock_level and not style.added:
                                            if style.name.lower().__contains__(
                                                    input_name.lower()) and style.size.lower().__contains__(
                                                input_size.lower()) and style.color.lower().__contains__(
                                                input_color.lower()):
                                                label.setText("Adding to cart...")
                                                start_open_link(time.time(), start_time, self.chrome_path,
                                                                style.generate()[style.size], style.name)
                                                style.setAdded(True)
                                                added = False
                                                product_list.pop(style_index)
                                                product_list.append(style)
                                                label.setText("Success: {:5.3f}s".format(time.time() - start_time))
                                                label.setStyleSheet(sheetGreen())
                                            else:

                                                style.setAdded(False)
                                        else:
                                            if style.name.lower().__contains__(
                                                    input_name.lower()) and style.size.lower().__contains__(
                                                input_size.lower()) and style.color.lower().__contains__(
                                                input_color.lower()):
                                                label.setText("Product OOS...")
                                                label.setStyleSheet(sheetRed())

                                        # If the stock level of the item changes
                                        if stock_level != old_stock_level:
                                            # If the item is in stock now
                                            if stock_level:
                                                if style.name.lower().__contains__(
                                                        input_name.lower()) and style.size.lower().__contains__(
                                                    input_size.lower()) and style.color.lower().__contains__(
                                                    input_color.lower()):
                                                    label.setText("Adding to cart...")
                                                    start_open_link(time.time(), start_time, self.chrome_path,
                                                                    style.generate()[style.size], style.name)
                                                    style.setAdded(True)
                                                    added = False
                                                    label.setText("Success: {:5.3f}s".format(time.time() - start_time))
                                                    label.setStyleSheet(sheetGreen())
                                                else:
                                                    style.setAdded(False)
                                            # Else item has sold out, print sold out
                                            else:
                                                if style.name.lower().__contains__(
                                                        input_name.lower()) and style.size.lower().__contains__(
                                                    input_size.lower()) and style.color.lower().__contains__(
                                                    input_color.lower()):
                                                    label.setText("Product OOS...")
                                                    label.setStyleSheet(sheetRed())
                                            product_list.pop(style_index)
                                            product_list.append(style)
                                    # Else, this is the first iteration usually, adds the item to the list
                                    else:
                                        # If the item is in stock and has not been opened yet
                                        if stock_level and not style.added:
                                            if style.name.lower().__contains__(
                                                    input_name.lower()) and style.size.lower().__contains__(
                                                input_size.lower()) and style.color.lower().__contains__(
                                                input_color.lower()):
                                                """
                                                NEED TO FIX CODE STOPPING ONCE THIS IS RAN 5/2/2020: 12PM
                                                FIXED ISSUE: 5/2/2020 3:25PM USING THREADING
                                                """
                                                label.setText("Adding to cart...")
                                                start_open_link(time.time(), start_time, self.chrome_path,
                                                                style.generate()[style.size], style.name)
                                                style.setAdded(True)
                                                added = False
                                                label.setText("Success: {:5.3f}s".format(time.time() - start_time))
                                                label.setStyleSheet(sheetGreen())
                                            else:
                                                style.setAdded(False)
                                        else:
                                            if style.name.lower().__contains__(
                                                    input_name.lower()) and style.size.lower().__contains__(
                                                input_size.lower()) and style.color.lower().__contains__(
                                                input_color.lower()):
                                                label.setText("Product OOS...")
                                                label.setStyleSheet(sheetRed())
                                        product_list.append(style)
                        # print(len(product_list))
            except Exception as e:
                print("[ERROR] {0}".format(sys.exc_info()))
        else:
            print("\n[ERROR] Please fill in the item name, color, and size.")

    def start_search(self, input_name, input_size, input_color, product_list):
        """
        Method to search Supreme's site and open the item in Supreme's "Checkout" page
        if the item is found and in stock.

        @param input_name: Product name
        @param input_size: Product size
        @param input_color: Product color
        @param product_list: Empty list to be filled with all products on Supreme's "new" category
        """
        if input_name != "" and input_color != "":
            print("\n[Status] Task {3} starting...\n[Status] Looking for -> [{2}] [{0}] [{1}]\n".format(input_name,
                                                                                                        input_size,
                                                                                                        input_color,
                                                                                                        input_name))
            try:
                added = True
                # While loop to continue until the item is opened in the user's Chrome browser
                while added:
                    # Set seed for the random to be different each iteration
                    seed(1)
                    # Set user-agent headers
                    agent = random.choice(user_agents)
                    self.desktop_headers['user-agent'] = agent[2:len(agent) - 3]
                    self.mobile_headers['user-agent'] = agent[2:len(agent) - 3]

                    # Set start time
                    start_time = time.time()

                    with requests.Session() as s:
                        data = json.loads(get_mobile_data(s, self.mobile_headers).text)

                        # Get all the products on /mobile_stock.json and add them to a list
                        mobile_products = []
                        for category, products in data['products_and_categories'].items():
                            if category == 'new' or category == 'Shoes':
                                for product in products:
                                    if product['name'].lower().__contains__(input_name.lower()):
                                        category_name = product['category_name']
                                        name = product['name']
                                        product_id = product['id']
                                        new_item = product['new_item']
                                        price = product['price']

                                        mobile_product = MobileStock(category_name=category_name, name=name,
                                                                     id=product_id,
                                                                     new_item=new_item,
                                                                     price=price)
                                        mobile_products.append(mobile_product)

                        # Search through all /product_id.json
                        for product in mobile_products:
                            data = json.loads(get_desktop_data(s, get_new_url(product.id), self.desktop_headers).text)

                            all_size_options = {}
                            item_name = product.name
                            atc_value = product.id

                            # Search through all product styles
                            for item in data['styles']:
                                # Search through all product sizes and checks stock level for each size
                                for size in item['sizes']:

                                    color = item['name']
                                    color_id = item['id']

                                    size_name = size['name']
                                    size_id = size['id']
                                    stock_level = size['stock_level']

                                    all_size_options[size_name] = [size_id, stock_level]
                                    style = Style(name=item_name, color=color, color_id=color_id, size=size_name,
                                                  size_id=size_id,
                                                  stock_level=stock_level, atc_value=atc_value,
                                                  all_sizes=all_size_options)

                                    result = exists_in_list(style, product_list)
                                    style_index = result[1]
                                    # If the item is in the list
                                    if result[0]:
                                        style.setAdded(result[2])
                                        old_stock_level = product_list[style_index].stock_level
                                        # If the item is in stock and the link has not opened yet, open it
                                        if stock_level and not style.added:
                                            if style.name.lower().__contains__(
                                                    input_name.lower()) and style.size.lower().__contains__(
                                                input_size.lower()) and style.color.lower().__contains__(
                                                input_color.lower()):
                                                start_open_link(time.time(), start_time, self.chrome_path,
                                                                style.generate()[style.size], style.name)
                                                style.setAdded(True)
                                                added = False
                                                product_list.pop(style_index)
                                                product_list.append(style)
                                            else:
                                                style.setAdded(False)
                                        # If the stock level of the item changes
                                        if stock_level != old_stock_level:
                                            # If the item is in stock now
                                            if stock_level:
                                                if style.name.lower().__contains__(
                                                        input_name.lower()) and style.size.lower().__contains__(
                                                    input_size.lower()) and style.color.lower().__contains__(
                                                    input_color.lower()):
                                                    start_open_link(time.time(), start_time, self.chrome_path,
                                                                    style.generate()[style.size], style.name)
                                                    style.setAdded(True)
                                                    added = False
                                                else:
                                                    style.setAdded(False)
                                            # Else item has sold out, print sold out
                                            else:
                                                continue
                                            product_list.pop(style_index)
                                            product_list.append(style)
                                    # Else, this is the first iteration usually, adds the item to the list
                                    else:
                                        freq = 1500
                                        duration = 1
                                        winsound.Beep(freq, duration)

                                        # If the item is in stock and has not been opened yet
                                        if stock_level and not style.added:
                                            if style.name.lower().__contains__(
                                                    input_name.lower()) and style.size.lower().__contains__(
                                                input_size.lower()) and style.color.lower().__contains__(
                                                input_color.lower()):
                                                start_open_link(time.time(), start_time, self.chrome_path,
                                                                style.generate()[style.size], style.name)
                                                style.setAdded(True)
                                                added = False
                                            else:
                                                style.setAdded(False)
                                        product_list.append(style)
                        # print(len(product_list))
            except Exception as e:
                print("[ERROR] {0}".format(sys.exc_info()))
        else:
            print("\n[ERROR] Please fill in the item name, color, and size.")

    # def start_monitor(self):
    #     """
    #     Method to monitor all products on Supreme for restocks
    #     """
    #     print("\n[RESTOCK] Started...")
    #     try:
    #         # While loop to constantly check for restocks
    #         while True:
    #             # Set seed for the random to be different each iteration
    #             seed(1)
    #             # Set user-agent headers
    #             agent = random.choice(get_chrome_user_agent())
    #             self.desktop_headers['user-agent'] = agent[2:len(agent) - 3]
    #             self.mobile_headers['user-agent'] = agent[2:len(agent) - 3]
    #
    #             # Set start time
    #             time_now = datetime.now()
    #
    #             with requests.Session() as s:
    #                 data = json.loads(get_mobile_data(s, self.mobile_headers).text)
    #
    #                 # Get all the products on /mobile_stock.json and add them to a list
    #                 mobile_products = []
    #                 for category, products in data['products_and_categories'].items():
    #                     if category == 'new' or category == 'Shoes':
    #                         for product in products:
    #                             category_name = product['category_name']
    #                             name = product['name']
    #                             product_id = product['id']
    #                             new_item = product['new_item']
    #                             price = product['price']
    #
    #                             mobile_product = MobileStock(category_name=category_name, name=name, id=product_id,
    #                                                          new_item=new_item,
    #                                                          price=price)
    #                             mobile_products.append(mobile_product)
    #
    #                 # Search through all /product_id.json
    #                 for product in mobile_products:
    #                     data = json.loads(get_desktop_data(s, get_new_url(product.id), self.desktop_headers).text)
    #
    #                     all_size_options = {}
    #                     item_name = product.name
    #                     atc_value = product.id
    #
    #                     # Search through all product styles
    #                     for item in data['styles']:
    #                         # Search through all product sizes and checks stock level for each size
    #                         for size in item['sizes']:
    #
    #                             color = item['name']
    #                             color_id = item['id']
    #
    #                             size_name = size['name']
    #                             size_id = size['id']
    #                             stock_level = size['stock_level']
    #
    #                             all_size_options[size_name] = [size_id, stock_level]
    #                             style = Style(name=item_name, color=color, color_id=color_id, size=size_name,
    #                                           size_id=size_id,
    #                                           stock_level=stock_level, atc_value=atc_value, all_sizes=all_size_options)
    #
    #                             result = exists_in_list(style, self.all_products)
    #                             style_index = result[1]
    #                             # If the item is in the list
    #                             if result[0]:
    #                                 style.setAdded(result[2])
    #                                 old_stock_level = self.all_products[style_index].stock_level
    #                                 # If the stock level of the item changes
    #                                 if stock_level != old_stock_level:
    #                                     # If the item is in stock now, print restocked
    #                                     if stock_level:
    #                                         print_item_restocked(style.name, style.color, time_now, style.generate())
    #                                     # Else item has sold out, print sold out
    #                                     else:
    #                                         print_item_sold_out(style.name, style.color, style.size, time_now)
    #                                     self.all_products.pop(style_index)
    #                                     self.all_products.append(style)
    #                             # Else, this is the first iteration usually, adds the item to the list
    #                             else:
    #                                 freq = 1500
    #                                 duration = 1
    #                                 winsound.Beep(freq, duration)
    #                                 self.all_products.append(style)
    #                 # print(len(self.all_products))
    #     except Exception as e:
    #         print("[RESTOCK ERROR] {0}".format(e))
    #
    # def start_specific_monitor(self, input_name, list_item):
    #     """
    #     Method to monitor a specific item for restocks on Supreme
    #     @param input_name: Product name
    #     @param list_item: Empty list to be filled with the input_name's data
    #     """
    #     print("\n[RESTOCK] Started...\n")
    #     print("[RESTOCK] Looking for [{0}]...\n".format(input_name))
    #     try:
    #         # While loop to constantly check for restocks
    #         while True:
    #             # Set seed for the random to be different each iteration
    #             seed(1)
    #             # Set user-agent headers
    #             agent = random.choice(get_chrome_user_agent())
    #             self.desktop_headers['user-agent'] = agent[2:len(agent) - 3]
    #             self.mobile_headers['user-agent'] = agent[2:len(agent) - 3]
    #             # Set start time
    #             time_now = datetime.now()
    #
    #             with requests.Session() as s:
    #                 data = json.loads(get_mobile_data(s, self.mobile_headers).text)
    #
    #                 # Get all the products on /mobile_stock.json and add them to a list
    #                 mobile_products = []
    #                 for category, products in data['products_and_categories'].items():
    #                     if category == 'new' or category == 'Shoes':
    #                         for product in products:
    #                             category_name = product['category_name']
    #                             name = product['name']
    #                             product_id = product['id']
    #                             new_item = product['new_item']
    #                             price = product['price']
    #                             if name.lower().__contains__(input_name.lower()):
    #                                 mobile_product = MobileStock(category_name=category_name, name=name, id=product_id,
    #                                                              new_item=new_item,
    #                                                              price=price)
    #                                 mobile_products.append(mobile_product)
    #
    #                 # Search through all /product_id.json
    #                 for product in mobile_products:
    #                     data = json.loads(get_desktop_data(s, get_new_url(product.id), self.desktop_headers).text)
    #
    #                     all_size_options = {}
    #                     item_name = product.name
    #                     atc_value = product.id
    #
    #                     # Search through all product styles
    #                     for item in data['styles']:
    #                         # Search through all product sizes and checks stock level for each size
    #                         for size in item['sizes']:
    #
    #                             color = item['name']
    #                             color_id = item['id']
    #
    #                             size_name = size['name']
    #                             size_id = size['id']
    #                             stock_level = size['stock_level']
    #
    #                             all_size_options[size_name] = [size_id, stock_level]
    #                             style = Style(name=item_name, color=color, color_id=color_id, size=size_name,
    #                                           size_id=size_id,
    #                                           stock_level=stock_level, atc_value=atc_value, all_sizes=all_size_options)
    #
    #                             result = exists_in_list(style, list_item)
    #                             style_index = result[1]
    #                             # If the item is in the list
    #                             if result[0]:
    #                                 style.setAdded(result[2])
    #                                 old_stock_level = list_item[style_index].stock_level
    #                                 # If the stock level of the item changes
    #                                 if stock_level != old_stock_level:
    #                                     # If the item is in stock now, print restocked
    #                                     if stock_level:
    #                                         print_item_restocked(style.name, style.color, time_now, style.generate())
    #                                     # Else item has sold out, print sold out
    #                                     else:
    #                                         print_item_sold_out(style.name, style.color, style.size, time_now)
    #                                     list_item.pop(style_index)
    #                                     list_item.append(style)
    #                             # Else, this is the first iteration usually, adds the item to the list
    #                             else:
    #                                 freq = 1500
    #                                 duration = 1
    #                                 winsound.Beep(freq, duration)
    #                                 list_item.append(style)
    #                 # print(len(self.all_products))
    #     except Exception as e:
    #         print(e)
