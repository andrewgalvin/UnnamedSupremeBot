class MobileStock:
    """
        A class used to create a Supreme Item and its corresponding checkout link.

        Attributes
        ----------
        name : str
            the item's name
        item_style_value : str
            the item's style number
        color : str
            the item's color
            *Note, a item's style number depends on it's color
        size_select_value : str
            the item's size value
            *Note, this come's from Supreme's drop down as seen below
        add_to_cart_value : str
            the item's specific add to cart value
        atc_link : str
            once the above variables are filled you are able to create a link to auto checkout

        Methods
        -------
        generate(self):
            generates the atc_link
    """
    global category_name
    global id
    global name
    global new_item
    global price
    global color

    def __init__(self, category_name, id, name, new_item, price):
        """
        Parameters
        ----------
        item : str
            the item's name
        item_style_value : str
            the item's style number
        color : str
            the item's color
            *Note, a item's style number depends on it's color
        size_select_value : str
            the item's size value
            *Note, this come's from Supreme's drop down as seen below
        add_to_cart_value : str
            the item's specific add to cart value
        """
        #Initialize the Supreme Item
        self.name = name
        self.id = id
        self.price = price
        self.new_item = new_item
        self.category_name = category_name

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return "\n----------\nCategory Name: {0}\nID: {1}\nName: {2}\nNew Item: {3}\nPrice: {4}\n----------\n".format(self.category_name, self.id, self.name, self.new_item, self.price)
