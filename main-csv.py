# ubah nama disetiap file di folder menjadi generate name berurutan
import os
import numpy
import colorama
from colorama import Fore
from PIL import Image                                                                                
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

	directoryOri = os.getcwd()+"/"+pathOri+"/"+val
	# directoryOri = os.getcwd()+"/"+pathOri+"/"+val.split()[1]
	numberx += 1
	for filename in os.listdir(directoryOri):
	    f = os.path.join(directoryOri, filename)
	    
	    img = mpimg.imread(pathOri+"/"+val+"/"+filename)
	    imgplot = plt.imshow(img)
	    plt.show()
	    # img = Image.open(pathOri+"/"+val+"/"+filename)
	    # img.show() untuk windo
	    print('==========================')
	    for x, i in enumerate(filename.split()):
	    	print(x, i)
	    print('==========================')
	    break

	ijudul = input("JUDUL DEPAN = ")
	if ijudul=='':
		ijudul = ''

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
	
	ikategori = input('''1. Tas selempang pria = 100570
2. Dompet lainya (pria) = 100613
3. Ransel Wanita = 100089
4. Clutch wanita = 100091
5. Tas Pinggang Wanita = 100092
6. Tote Bag = 100093
7. Top Handle Bag  = 100094
8. Tas Selempang & Bahu Wanita = 100095
9. Dompet Wanita -> Dompet Kunci & Handphone = 100340
10. Dompet Wanita -> Dompet Lipat = 100341
11. Dompet Wanita -> Dompet Panjang = 100342
12. Dompet Wanita -> Dompet Wanita Lainnya = 100343
13. Tas Wanita Lainnya = 100098

Pilih kode =''')

	if ikategori=='':
		ikategori = 100098
	elif ikategori == 1:
		ikategori = 100570
	elif ikategori == 2:
		ikategori = 100613
	elif ikategori == 3:
		ikategori = 100089
	elif ikategori == 4:
		ikategori = 100091
	elif ikategori == 5:
		ikategori = 100092
	elif ikategori == 6:
		ikategori = 100093
	elif ikategori == 7:
		ikategori = 100094
	elif ikategori == 8:
		ikategori = 100095
	elif ikategori == 9:
		ikategori = 100340
	elif ikategori == 10:
		ikategori = 100341
	elif ikategori == 11:
		ikategori = 100342
	elif ikategori == 12:
		ikategori = 100343
	elif ikategori == 13:
		ikategori = 100098
	else:
		ikategori = 100098

	for filename in os.listdir(directoryOri):
	    f = os.path.join(directoryOri, filename)
	    # checking if it is a file
		
	    if os.path.isfile(f):
	        filenameold, formatfileold = os.path.splitext(f) 			
	        # ambil kode dari file name
	        kode = val
	        numeric_string = "".join(filter(str.isdigit, kode))
	        newDirectoryOri = (directoryOri + kode + "/" + filename)
	        
	        print("Full : " + str(splitFileName(filename)))
	        print("Kode : " + splitFileName(filename)[0])
	        harga = splitFileName(filename)[int(iharga)].replace("IDR","").replace(".","")
	        print("Harga : " + str(harga))
	        
	        bahan = (splitFileName(filename)[int(ibahan)] +" " +splitFileName(filename)[int(ibahan2)])
	        print("Bahan : "+bahan)
	        splitSize = (str(splitFileName(filename)[int(isize)]).split('X'))
	        print("Varian : " + splitFileName(filename)[int(ivarian)])
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
	        berat = (splitFileName(filename)[int(iberat)][:-2])
	        varian, formatvarian = os.path.splitext(splitFileName(filename)[int(ivarian)])
	        # rumus deskripsi = detail ukuran, penjelasan bahan, penjelasan fitur/fungsi/membagus2 kan, cara perawatan
	        # rumus judul = jenis tas + wanita + import + | keyword lainya + kode
	        judulLengkap = str(ijudul) + " - TAS IMPORT BAHAN " + bahan + " - " + str(numeric_string)
	        deskripsi = '''"Tas ini sangat cocok untuk kamu yang ingin tampil cantik, menarik dan pastinya fashionable daripada yang lain tidak hanya itu sangat nyaman digunakan untuk Hangout atau Jalan-jalan/Traveling

Info :
Panjang = '''+panjang+'''
Tinggi = '''+tinggi+'''
Lebar = '''+lebar+'''
Berat = '''+berat+'''gr
Bahan = '''+bahan+'''

PENJELASAN BAHAN PU (Polyurethane)
Polyurethane adalah suatu bahan campuran atau hasil pengisolvenan antara karet dan plastik sehingga didapatkan pelarutan material yang memiliki keunggulan sangat tahan gesek, tahan aus, tahan terhadap beberapa kimia ringan, stabil dalam suhu dingin dan panas. Walaupun termasuk jenis imitasi, namun bahan tersebut dikenal baik tahan lama.

CARA PERAWATAN TAS YANG BAIK
Jangan simpan di tempat yang lembab. Untuk perawatan sebaiknya hindari penyimpanan tas berimitasi dan kulit ditempat lembab. Simpan ditempat kering dan terkena angin. Hal ini untuk mengindarkan dari kerusakan pada tas berbahan imitasi ataupun kulit, bersihkan tas secara berkala dari debu-debu yang menempel.

NB : 
Masukan Warna Alternatif lain di catatan ketika Anda Pesan, ini akan menjadi warna alternatif pilihan anda jika warna yang di pesan tidak ada, jika tidak memasukan warna Alternatif kami akan kirim warna lainya,

*Jika memberi Rating dibawah 3 tanpa alasan yang jelas mohon maaf kami akan blokir jadi jika ada keluhan bisa chat/hubungi kami

#tasimport #taswanita #tasperempuan #tasoriginal #tasasli #tasmurah #tasselempang #tascantik
	        "'''
	        gambar1 = '"https://member.remotebisnis.com/sp/' + str(kode) + '/'+str(kode)+'.png"'
	        gambar2 = '"https://member.remotebisnis.com/sp/' + str(kode) + '/img-1.jpg"'
	        gambar3 = '"https://member.remotebisnis.com/sp/' + str(kode) + '/img-2.jpg"'
	        gambar4 = '"https://member.remotebisnis.com/sp/' + str(kode) + '/img-3.jpg"'
	        gambar5 = '"https://member.remotebisnis.com/sp/' + str(kode) + '/img-4.jpg"'
	        gambar6 = '"https://member.remotebisnis.com/sp/' + str(kode) + '/img-5.jpg"'
	        gambar7 = '"https://member.remotebisnis.com/sp/' + str(kode) + '/img-6.jpg"'
	        gambar8 = '"https://member.remotebisnis.com/sp/' + str(kode) + '/img-7.jpg"'
	        gambar9 = '"https://member.remotebisnis.com/sp/' + str(kode) + '/img-8.jpg"'

	        data = numpy.append(data, [[ikategori, judulLengkap, deskripsi, '', 'No (ID)', numberx, 'Warna', varian, '', '', '', harga, '20', '', '', gambar1, gambar2, gambar3, gambar4, gambar5, gambar6, gambar7, gambar8, gambar9, berat, '', '', '', '', 'Aktif', '', '']], axis = 0)
	print("-------------------------------")
	print(" ")
	print(" ")
	print(" ")
	print(" ")
	# os.system('cls')
	os.system('clear')


numpy.savetxt("countries.csv", data, delimiter=',', comments="", fmt = '%s')