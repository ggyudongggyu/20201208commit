from MailSender import MailSender
from namecheker import NameCheck

class WeeklyGiftSender:
    def __init__(self, add, path, password):
        self.address = add
        self.path = path
        self.msender = MailSender(self.address, password)

    def send_all(self):

        # for filename in file_list:
        # if name_check() == True:

        if filename in file_list:
            self.msender.send(to, file_path)

            #filename はフルパスで

#main.py に
wsender = WeeklyGiftSender(add, path, password)
wsender.send_all()
