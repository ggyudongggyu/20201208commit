import os

file_path = 'C:\Users\i3_OWNER's\Documents\python_ruby\practice\tcs\'
file_names = os.listdir(file_path)
file_names


for x in member_name:
    src = os.path.join(file_path, '')
    dst = x + '.xlsx'

    shutil.copy('sample.xlsx', '%s.xlsx' %(x))

for name in file_names:
    src = os.path.join(file_path, name)
    for x in member_name:
    dst = str(i) + '.xlsx'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
