import shutil
import os

class CP:
    def __init__(self, name_lists):
        self.name_lists = name_lists
        self.copy()
    def copy(self):
        # if
        if os.path.exists('weekly_gift_sample.json'):
            for name in self.name_lists:
                shutil.copy2("./sample.json", "./weekly_gift_%s.json" %(name))
        else:
            print('sample json file does not exists.')
            
