# ubah nama disetiap file di folder menjadi generate name berurutan
import os
import numpy
import colorama
from colorama import Fore
from PIL import Image                                                                                

# Get the list of all files and directories
path = "KATALOG_SEMUA_TAS_DONE"
pathOri = "KATALOG_SEMUA_TAS_ORINAME"

dir_list = os.listdir(path)
limitLoop = 2
newDirectoryOri = ''

data = numpy.array([['Kategori', 'Nama Produk', 'Deskripsi Produk', 'SKU Induk', 'Produk Berbahaya', 'Kode Integrasi Variasi', 'Nama Variasi 1', 'Varian untuk Variasi 1', 'Foto Produk per Varian', 'Nama Variasi 2', 'Varian untuk Variasi 2', 'Harga', 'Stok', 'Kode Variasi', 'Panduan Ukuran', 'Foto Sampul', 'Foto Produk 1', 'Foto Produk 2', 'Foto Produk 3', 'Foto Produk 4', 'Foto Produk 5', 'Foto Produk 6', 'Foto Produk 7', 'Foto Produk 8', 'Berat', 'Panjang', 'Lebar', 'Tinggi', 'Next Day', 'Reguler (Cashless)', 'Hemat', 'Dikirim Dalam Pre-order']])

def splitFileName (fn):
	return fn.split(' ')

numberx = 0
for val in dir_list:
	if numberx == limitLoop :
		break

	directoryOri = os.getcwd()+"/"+pathOri+"/"+val.split()[1]
	numberx += 1

	for filename in os.listdir(directoryOri):
	    f = os.path.join(directoryOri, filename)
	    img = Image.open(pathOri+"/"+val.split()[1]+"/"+filename)
	    img.show()
	    print(filename)
	    break

	ijudul = input("JUDUL DEPAN = ")
	if ijudul=='':
		ijudul = 1

	iharga = input("harga = ")
	if iharga=='':
		iharga = 1

	ibahan = input("bahan = ")
	if ibahan=='':
		ibahan = 2
		
	ibahan2 = input("bahan2 = ")
	if ibahan2=='':
		ibahan2 = 3
		
	isize = input("size = ")
	if isize=='':
		isize = 5
		
	iberat = input("berat = ")
	if iberat=='':
		iberat = 7
		
	ivarian = input("varian = ")
	if ivarian=='':
		ivarian = 9

	for filename in os.listdir(directoryOri):
	    f = os.path.join(directoryOri, filename)
	    # checking if it is a file
		
	    if os.path.isfile(f):
	        filenameold, formatfileold = os.path.splitext(f) 			
	        # ambil kode dari file name
	        kode = splitFileName(val)[1]
	        newDirectoryOri = (directoryOri + kode + "/" + filename)
	        
	        print("Full : " + str(splitFileName(filename)))
	        print("Kode : " + splitFileName(filename)[0])
	        harga = splitFileName(filename)[iharga].replace("IDR","").replace(".","")
	        print("Harga : " + harga)
	        
	        bahan = (splitFileName(filename)[ibahan] +" - " +splitFileName(filename)[ibahan2])
	        print("Bahan : "+bahan)
	        splitSize = (str(splitFileName(filename)[isize]).split('X'))
	        print("Varian : " + splitFileName(filename)[ivarian])
	        print("Size : ")

	        numberSize = 0
	        tinggi = ''
	        lebar = ''
	        panjang = ''
	        for x in splitSize:
	        	if numberSize == 0:
	        		lebar =(x.replace('L','')+'CM')
	        	elif numberSize == 1:
	        		tinggi =(x.replace('H','')+"CM")
	        	elif numberSize == 2:
	        		panjang =(x.replace('W',''))

	        	numberSize+=1
	        berat = (splitFileName(filename)[iberat][:-2])
	        varian = splitFileName(filename)[ivarian]
	        # rumus deskripsi = detail ukuran, penjelasan bahan, penjelasan fitur/fungsi/membagus2 kan, cara perawatan
	        # rumus judul = jenis tas + wanita + import + | keyword lainya + kode
	        
	        # header = ['Kategori', 'Nama Produk', 'Deskripsi Produk', 'SKU Induk', 'Produk Berbahaya', 'Kode Integrasi Variasi', 'Nama Variasi 1', 'Varian untuk Variasi 1', 'Foto Produk per Varian', 'Nama Variasi 2', 'Varian untuk Variasi 2', 'Harga', 'Stok', 'Kode Variasi', 'Panduan Ukuran', 'Foto Sampul', 'Foto Produk 1', 'Foto Produk 2', 'Foto Produk 3', 'Foto Produk 4', 'Foto Produk 5', 'Foto Produk 6', 'Foto Produk 7', 'Foto Produk 8', 'Berat', 'Panjang', 'Lebar', 'Tinggi', 'Next Day', 'Reguler (Cashless)', 'Hemat', 'Dikirim Dalam Pre-order']

	        # header = ['Kategori', 'Nama Produk', 'Deskripsi Produk', 'SKU Induk', 'Produk Berbahaya', 'Kode Integrasi Variasi', 'Nama Variasi 1', 'Varian untuk Variasi 1', 'Foto Produk per Varian', 'Nama Variasi 2', 'Varian untuk Variasi 2', 'Harga', 'Stok', 'Kode Variasi', 'Foto Sampul', 'Foto Produk 1', 'Foto Produk 2', 'Foto Produk 3', 'Foto Produk 4', 'Foto Produk 5', 'Foto Produk 6', 'Foto Produk 7', 'Foto Produk 8', 'Berat', 'Panjang', 'Lebar', 'Tinggi', 'Reguler (Cashless)', 'Dikirim Dalam Pre-order']


			numeric_filter = filter(str.isdigit, kode)
			numeric_string = "".join(numeric_filter)

	        judulLengkap = ijudul + " | " + numeric_string
	        data = numpy.append(data, [[1112, judulLengkap, '', '', 'No (ID)', numberx, 'Warna', varian, '', '', '', harga, '20', '', 'gambar sampul url', '', '', '', '', '', '', '', '', berat, '', '', '', 'Aktif', '', '', '', '']], axis = 0)
	print("-------------------------------")
	os.system('clear')


numpy.savetxt("countries.csv", data, delimiter=',', comments="", fmt = '%s')