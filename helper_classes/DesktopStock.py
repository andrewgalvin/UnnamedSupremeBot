class DesktopStock:

    global add_to_cart_id
    global item_id
    global size_id
    global name
    global color

    def __init__(self, name, add_to_cart_id, item_id, size_id, color):
        self.name = name
        self.add_to_cart_id = add_to_cart_id
        self.item_id = item_id
        self.size_id = size_id
        self.color = color
    def __str__(self):
        return "\n----------\nName: {0}\nAdd to Cart ID: {1}\nItem ID: {2}\nSize ID: {3}\nColor: {4}\n----------\n".format(self.name, self.add_to_cart_id, self.item_id, self.size_id, self.color)
