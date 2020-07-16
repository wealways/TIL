import os


os.chdir(r'C:\Users\aclass\Desktop\file_practice\dummy')

filenames=os.listdir('.')

for name in filenames:
    new_filename = name.replace('samsung_','SSAFY_')
    os.rename(name, new_filename)


print('good!')