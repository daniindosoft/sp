# ubah nama disetiap file di folder menjadi generate name berurutan
import os
 
# Get the list of all files and directories
path = "KATALOG_SEMUA_TAS_ORINAME-1"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
numberx = 0
for val in dir_list:
	directory = os.getcwd()+"/"+path+"/"+val
	numberx = 0
	for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    # checking if it is a file
	    if os.path.isfile(f):
	        filenameold, formatfileold = os.path.splitext(f) 
	        newfilename = directory+"/img-"+str(numberx)+formatfileold
	        os.rename(f, newfilename)
	    numberx += 1