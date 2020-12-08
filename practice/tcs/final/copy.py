import shutil

class CP:
    def __init__(self, name_lists):
        self.name_lists = name_lists
        self.copy()
    def copy(self):
        # if
        # os.path.exits('sample.pdf')
        for i in range(len(name_lists)):
            shutil.copy2("./sample.xlsx", "./sample%s.xlsx" %(i))
