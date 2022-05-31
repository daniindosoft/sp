# looop folder , buat folder by name kode lalu copy name file tersebut ke folder yg dibuat
#!/usr/bin/python -tt
import shutil
import os
# assign directory
directory = 'TAS'
 
# iterate over files in
# that directory

arrayFolder = []

# create array foldername
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        arrayFolder.append(f.split()[0])

# buat filder
for xx in arrayFolder:
	if not os.path.exists(xx):
	    os.mkdir(xx)

# move file
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        shutil.move(f, f.split()[0]+"/"+filename)