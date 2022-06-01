# cari folder path lalu file disitu di pindahkan ke folder yg nma nya sama dengan nama file
#!/usr/bin/python -tt
import shutil
import os
import glob
import pathlib

# assign directory
path = 'KATALOG_SEMUA_TAS_BELUM'
dir_list = os.listdir(path)

# iterate over files in
# that directory
os.system('clear')
num = 0
for val in dir_list:
	directory = os.getcwd()+"/"+path+"/"+val
	if len(directory.split('.')) > 1:
		num +=1
		# print(directory[:-1])
		# print(str(num)+'.'+str(directory.split()[1]))
		firstname = directory.split()[0][:-1]
		file_extension, formatfile = os.path.splitext(directory)
		nameplace = (directory[:-3].replace('.','')+"/"+os.path.basename(directory))
		file = pathlib.Path(file_extension)
		print(file)
		if file.exists ():
			print('file asli = ' + directory)
			print('file move = ' + nameplace)
			print('----------')
			newdir = (os.getcwd()+"/"+path+"/"+"done "+os.path.basename(directory).split('.')[0])
			shutil.move(directory, nameplace)
			os.rename(file_extension, newdir)
		else:
		    print ("File not exist")
