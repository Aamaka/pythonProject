class Cart:
    def __init__(self, limit):
        self.limit = limit - 1
        self.item = []

    def add_item(self, item):
        if len(self.item) > self.limit:
            self.item.pop(0)
            self.item.insert(0, item)
        else:
            self.item.append(item)
