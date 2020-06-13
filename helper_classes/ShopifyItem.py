class ShopifyItem:
    global id
    global title
    global size
    
    def __init__(self, id, title, size):
        self.id = id
        self.title = title
        self.size = size

    def setAdded(self, added):
        self.added = added

    def getAdded(self):
        return self.added
    
    def __str__(self):
        return "Title: {0}\n Size: {1}\n ID: {2}\n".format(self.title, self.size, self.id)

    # def generate(self):
    #     atc_bz = "https://atc.bz/p?a=a&b=&p="
    #     atc_link = {}
    #     for key, value in self.all_sizes.items():
    #         if value[1]:
    #             atc_link[key] = "{0}{1}&st={2}&s={3}&c= \n".format(atc_bz, self.atc_value, self.color_id,
    #                                                                value[0])
    # 
    #     return atc_link
