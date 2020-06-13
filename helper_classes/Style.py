class Style:
    global name
    global color
    global color_id
    global size
    global size_id
    global stock_level
    global atc_value
    global all_sizes

    def __init__(self, name, color, color_id, size, size_id, stock_level, atc_value, all_sizes):
        self.added = False
        self.all_sizes = all_sizes
        self.atc_value = atc_value
        self.stock_level = stock_level
        self.size_id = size_id
        self.size = size
        self.color_id = color_id
        self.color = color
        self.name = name

    def setAdded(self, added):
        self.added = added

    def getAdded(self):
        return self.added
    def __str__(self):
        return "Name: {0}, Color: {1}, Color ID: {2}, Size: {3}, Size ID: {4}, Stock = {5}, ATC Value = {6}".format(
            self.name,
            self.color,
            self.color_id,
            self.size,
            self.size_id,
            self.stock_level,
            self.atc_value)

    def generate(self):
        atc_bz = "https://atc.bz/p?a=a&b=&p="
        atc_link = {}
        for key, value in self.all_sizes.items():
            if value[1]:
                atc_link[key] = "{0}{1}&st={2}&s={3}&c= \n".format(atc_bz, self.atc_value, self.color_id,
                                                                   value[0])

        return atc_link
