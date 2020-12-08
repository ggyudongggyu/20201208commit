import re
import os,sys
import glob
os.chdir('C:\\Users\\i3_OWNER\'s\\Documents\\pytest')
file_list = glob.glob("*.json")
for filename in file_list:
    check_filename = re.findall(r'^Weekly_Gift_+\w+.json',filename)
if check_filename:
    print("file is checked and sending now.")
    #mailsender()
else:
    print("file name is not appropriate. Follow the format.")
