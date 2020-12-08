class Student:
    def __init__(self):
        self.bag = None
    def putItem(self, pocket_number, item_name):
        if pocket_number == 1:
            self.bag.pocket1 = item_name
        elif pocket_number == 2:
            self.bag.pocket2 = item_name
        elif pocket_number == 3:
            self.bag.pocket3 = item_name
        else:
            self.bag.pocket4 = item_name
        # self.pocekt_number = pocket_number
        # self.item_name = item_name
