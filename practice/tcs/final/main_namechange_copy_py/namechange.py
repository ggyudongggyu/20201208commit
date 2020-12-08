import os

class CH:
    def __init__(self, path, name_lists):
        self.name_lists = name_lists
        self.path = path
        self.nameChange()
    def nameChange(self):
        for filename in os.listdir(path):
            i = 0
            os.rename(path+filename, path+str(name_lists[i])+'xlsx')
            i += 1
