import os

class NameCheck:
    def __init__(self, name_lists):
        self.name_lists = name_lists
        self.name_check()
    def name_check(self):
            if os.path.isfile('C:\\Users\\i3_OWNER\'s\\Documents\\pytest\\Weekly_Gift.csv'):
                return
            else:
                print("no file")


            # if os.path.exists('C:\\Users\\i3_OWNER\'s\\Documents\\pytest\\Weekly_Gift_%s.json' %(x)):
            #     print("file exists")
            # else:
            #     print("no file")


#
# name_lists = ['park', 'soneshin', 'komori', 'lee', 'mawatari']
# for x in name_lists:
#     os.path.isfile('C:\\Users\\i3_OWNER\'s\\Documents\\pytest\\Weekly_Gift_%s.json' %(x))
