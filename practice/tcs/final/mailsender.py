
class MS:
    def __init__(self, your_emailaddress, folder_path):
        self.my_address = your_emailaddress
        file_lists = []
        self.folder_path = folder_path  #weekly giftがある場所

        if os.path.exists('folder_name'):
            for name in self.name_lists:
                shutil.copy2("./sample.json", "./weekly_gift_%s.json" %(name))
        else:
            print('sample json file does not exists.')
