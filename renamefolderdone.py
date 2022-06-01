# cari folder path lalu file disitu di pindahkan ke folder yg nma nya sama dengan nama file
#!/usr/bin/python -tt
import shutil
import os
import glob
import pathlib

# assign directory
path = 'KATALOG_SEMUA_TAS_ORINAME_DONE'
dir_list = os.listdir(path)

# iterate over files in
# that directory
os.system('cls')
num = 0
for val in dir_list:
	directory = os.getcwd()+"/"+path+"/"+val
	newname = (directory.replace('done ',''))
	os.rename(directory, newname)