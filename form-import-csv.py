# importing libraries
import os
import numpy
import colorama
from colorama import Fore
from PIL import Image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
import datetime

import sys

# arrayKode
# arrayJudul
# arrayHarga
# arrayBahan
# arrayBahan2
# arrayVarian
# arrayBerat
# arraySize
# arrayKategori
class Window(QDialog):
  
    # constructor
    def __init__(self):
        super(Window, self).__init__()
        # yg done, folder harus yg udh done
        self.path = "KATALOG_SEMUA_TAS_DONE"
        # yg nama masih ori
        self.pathOri = "KATALOG_SEMUA_TAS_ORINAME"

        print('.')
        print('.')
        print('APLIKASI BERJALAN ...........')
        self.dari = input("Dari = ")
        self.sampai = input("Sampai = ")
        self.dir_list = sorted(os.listdir(self.path))

        self.limitLoop = 10
        self.newDirectoryOri = ''
        self.itemkategori = ''
        self.data = numpy.array([['Kategori', 'Nama Produk', 'Deskripsi Produk', 'SKU Induk', 'Produk Berbahaya', 'Kode Integrasi Variasi', 'Nama Variasi 1', 'Varian untuk Variasi 1', 'Foto Produk per Varian', 'Nama Variasi 2', 'Varian untuk Variasi 2', 'Harga', 'Stok', 'Kode Variasi', 'Panduan Ukuran', 'Foto Sampul', 'Foto Produk 1', 'Foto Produk 2', 'Foto Produk 3', 'Foto Produk 4', 'Foto Produk 5', 'Foto Produk 6', 'Foto Produk 7', 'Foto Produk 8', 'Berat', 'Panjang', 'Lebar', 'Tinggi', 'Next Day', 'Reguler (Cashless)', 'Hemat', 'Dikirim Dalam Pre-order']])
        
        self.numberx = 0

        # setting window title
        self.setWindowTitle("Python")
        
        self.kode = {}
        self.judul = {}
        self.harga = {}
        self.bahan = {}
        self.bahan2 = {}
        self.varian = {}
        self.berat = {}
        self.size = {}
        self.bahantext = {}
        self.kategori = {}
        self.itemname = []
        self.btnm1 = {}
        self.btnp1 = {}
    
        # index cbox
        self.hargaIndexDefault = 1
        self.bahanIndexDefault = 2
        self.bahan2IndexDefault = 3
        self.sizeIndexDefault = 5
        self.beratIndexDefault = 7
        self.varianIndexDefault = 9
        # setting geometry to the window
        self.setGeometry(100, 100, 400, 600)
  
        # creating a group box
        
        self.formGroupBox = QGroupBox("Form 1")

        # creating spin box to select age
        self.ageSpinBar = QSpinBox()
  
        # creating combo box to select degree

        # creating a line edit
        self.nameLineEdit = QLineEdit()
  
        # calling the method that create the form
        self.createForm()
  
        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
  
        # adding action when form is accepted
        
  
        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)
  
        # creating a vertical layout
        mainLayout = QVBoxLayout()
  
        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)
  
        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)
  
        # setting lay out
        self.setLayout(mainLayout)
  
    # get info method called when form is accepted

    def simpan (self):
        self.data = numpy.array([['Kategori', 'Nama Produk', 'Deskripsi Produk', 'SKU Induk', 'Produk Berbahaya', 'Kode Integrasi Variasi', 'Nama Variasi 1', 'Varian untuk Variasi 1', 'Foto Produk per Varian', 'Nama Variasi 2', 'Varian untuk Variasi 2', 'Harga', 'Stok', 'Kode Variasi', 'Panduan Ukuran', 'Foto Sampul', 'Foto Produk 1', 'Foto Produk 2', 'Foto Produk 3', 'Foto Produk 4', 'Foto Produk 5', 'Foto Produk 6', 'Foto Produk 7', 'Foto Produk 8', 'Berat', 'Panjang', 'Lebar', 'Tinggi', 'Next Day', 'Reguler (Cashless)', 'Hemat', 'Dikirim Dalam Pre-order', 'Harga asli', 'Margin', 'Total']])
        
        numbervar = 1
        for x in self.harga:
            # print(self.harga[x].currentText())
            kode = self.kode[x].currentText()
            numeric_string = "".join(filter(str.isdigit, kode))
            
            margin = 15000
            harga = int(self.harga[x].currentText().replace("IDR","").replace(".",""))
            total = int(self.harga[x].currentText().replace("IDR","").replace(".","")) + margin
            bahan = (self.bahan[x].currentText() +" " +self.bahan2[x].currentText())
            bahantext = (self.bahantext[x].currentText())
            splitSize = (str(self.size[x].currentText()).split('X'))
            berat = (self.berat[x].currentText()[:-2])
            varian, formatvarian = os.path.splitext(self.varian[x].currentText())
            varianIndex = (self.varian[x].currentIndex())
            # SHOPEE MAX JUDUL = 255
            judulLengkap = str(self.judul[x].text()) + " - BAHAN " + bahan + " - " + str(numeric_string)
            ikategori = self.kategori[x].currentText().split('=')[1]
            directoryOri = os.getcwd()+"/"+self.pathOri+"/"+kode
            
            for filename in os.listdir(directoryOri):
                f = os.path.join(directoryOri, filename)
                if os.path.isfile(f):
                    
                    varianNow = f.split()[varianIndex][:-4]
                    # print(f)
                    # print(varianIndex)
                    # print(varianNow)
                    # print('----')
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

                    if bahantext == 'pu':
                        valbahantext = '''PENJELASAN BAHAN PU (Polyurethane)
Polyurethane adalah suatu bahan campuran atau hasil pengisolvenan antara karet dan plastik sehingga didapatkan pelarutan material yang memiliki keunggulan sangat tahan gesek, tahan aus, tahan terhadap beberapa kimia ringan, stabil dalam suhu dingin dan panas. Walaupun termasuk jenis imitasi, namun bahan tersebut dikenal baik tahan lama.

CARA PERAWATAN TAS YANG BAIK
Jangan simpan di tempat yang lembab. Untuk perawatan sebaiknya hindari penyimpanan tas berimitasi dan kulit ditempat lembab. Simpan ditempat kering dan terkena angin. Hal ini untuk mengindarkan dari kerusakan pada tas berbahan imitasi ataupun kulit, bersihkan tas secara berkala dari debu-debu yang menempel.'''
                    elif bahantext == 'ox':
                        valbahantext = "Terbuat dari bahan Oxford yang mana bahan ini dapat tahan terhadap air sehingga sangat cocok untuk aktifitas atau kegiatan diluar ruangan"

                    deskripsi = '''"Tas ini sangat cocok untuk kamu yang ingin tampil cantik, menarik dan pastinya fashionable daripada yang lain tidak hanya itu sangat nyaman digunakan untuk Hangout atau Jalan-jalan/Traveling

Info :
Panjang = '''+panjang+'''
Tinggi = '''+tinggi+'''
Lebar = '''+lebar+'''
Berat = '''+berat+'''gr
Bahan = '''+bahan+'''

'''+valbahantext+'''

NB : 
Masukan Warna Alternatif lain di catatan ketika Anda Pesan, ini akan menjadi warna alternatif pilihan anda jika warna yang di pesan tidak ada, jika tidak memasukan warna Alternatif kami akan kirim warna lainya,

*Jika memberi Rating dibawah 3 tanpa alasan yang jelas mohon maaf kami akan blokir jadi jika ada keluhan bisa chat/hubungi kami

#tasimport #taswanita #tasperempuan #tasoriginal #tasasli #tasmurah #tasselempang #tascantik
                    "'''
                    countVarians = len([name for name in os.listdir(directoryOri) if os.path.isfile(os.path.join(directoryOri, name))])

                    gambar1 = ''
                    gambar2 = ''
                    gambar3 = ''
                    gambar4 = ''
                    gambar5 = ''
                    gambar6 = ''
                    gambar7 = ''
                    gambar8 = ''
                    gambar9 = ''

                    for x in range(countVarians):
                        if x == 0:
                            gambar1 = 'https://member.remotebisnis.com/sp/done '+str(kode) + '/img-0.jpg'
                        if x == 1:
                            gambar2 = 'https://member.remotebisnis.com/sp/done '+str(kode) + '/img-1.jpg'
                        if x == 2:
                            gambar3 = 'https://member.remotebisnis.com/sp/done '+str(kode) + '/img-2.jpg'
                        if x == 3:
                            gambar4 = 'https://member.remotebisnis.com/sp/done '+str(kode) + '/img-3.jpg'
                        if x == 4:
                            gambar5 = 'https://member.remotebisnis.com/sp/done '+str(kode) + '/img-4.jpg'
                        if x == 5:
                            gambar6 = 'https://member.remotebisnis.com/sp/done '+str(kode) + '/img-5.jpg'
                        if x == 6:
                            gambar7 = 'https://member.remotebisnis.com/sp/done '+str(kode) + '/img-6.jpg'
                        if x == 7:
                            gambar8 = 'https://member.remotebisnis.com/sp/done '+str(kode) + '/img-7.jpg'

                    cover = '"https://member.remotebisnis.com/sp/done ' + str(kode) + '/'+str(kode)+'.png"'
                    # gambar2 = '"https://member.remotebisnis.com/sp/done ' + str(kode) + '/img-1.jpg"'
                    # gambar3 = '"https://member.remotebisnis.com/sp/done ' + str(kode) + '/img-2.jpg"'
                    # gambar4 = '"https://member.remotebisnis.com/sp/done ' + str(kode) + '/img-3.jpg"'
                    # gambar5 = '"https://member.remotebisnis.com/sp/done ' + str(kode) + '/img-4.jpg"'
                    # gambar6 = '"https://member.remotebisnis.com/sp/done ' + str(kode) + '/img-5.jpg"'
                    # gambar7 = '"https://member.remotebisnis.com/sp/done ' + str(kode) + '/img-6.jpg"'
                    # gambar8 = '"https://member.remotebisnis.com/sp/done ' + str(kode) + '/img-7.jpg"'
                    # gambar9 = '"https://member.remotebisnis.com/sp/done ' + str(kode) + '/img-8.jpg"'
                    
                    self.data = numpy.append(self.data, [[ikategori, judulLengkap, deskripsi, '', 'No (ID)', numbervar, 'Warna', varianNow, '', '', '', total, '15', '', '', cover, gambar1, gambar2, gambar3, gambar4, gambar5, gambar6, gambar7, gambar8, berat, '', '', '', '', 'Aktif', '', '', harga, margin, total]], axis = 0)
            numbervar += 1
        
        datetimenow = datetime.datetime.now()
        dateStrName = (str(datetimenow).split('.')[0].replace(':','').replace(' ','_'))

        filenamecsv = 'shopee_import_'+str(self.dari)+'-'+str(self.sampai)+'-'+dateStrName+'.csv'
        open(filenamecsv, 'w')
        numpy.savetxt(filenamecsv, self.data, delimiter=',', comments="", fmt = '%s')
        print("Berhasil !!")


    def minCurrentIndex (self,x):
        self.harga[x].setCurrentIndex(self.hargaIndexDefault-1)
        
        self.bahan[x].setCurrentIndex(self.bahanIndexDefault-1)
        
        self.bahan2[x].setCurrentIndex(self.bahan2IndexDefault-1)
        
        self.varian[x].setCurrentIndex(self.varianIndexDefault-1)

        self.berat[x].setCurrentIndex(self.beratIndexDefault-1)

        self.size[x].setCurrentIndex(self.sizeIndexDefault-1)

    def plusCurrentIndex (self,x):
        
        self.harga[x].setCurrentIndex(self.hargaIndexDefault+1)
        
        self.bahan[x].setCurrentIndex(self.bahanIndexDefault+1)
        
        self.bahan2[x].setCurrentIndex(self.bahan2IndexDefault+1)
        
        self.varian[x].setCurrentIndex(self.varianIndexDefault+1)
        
        self.berat[x].setCurrentIndex(self.beratIndexDefault+1)

        self.size[x].setCurrentIndex(self.sizeIndexDefault+1)

    def splitFileName (fn):
        return fn.split(' ')

    def onchange(self,x):
        nowtext = self.judul[x]
        lentext = len(nowtext.text()) + 30
        print(lentext)
        if int(lentext) >= 255:
            print('over')
            nowtext.setStyleSheet('border:1px solid red')
        else:
            nowtext.setStyleSheet('border:1px solid black')

    # creat form method
    def createForm(self):
  
        # creating a form layout
        layout = QFormLayout()
        # adding rows
        # for name and adding input text

        self.itemkategori = ["1. Tas Selempang & Bahu Wanita =100095","2. Dompet lainya (pria) =100613","3. Ransel Wanita =100089","4. Clutch wanita =100091","5. Tas Pinggang Wanita =100092","6. Tote Bag =100093","7. Top Handle Bag  =100094","8. Tas selempang pria =100570","9. Dompet Wanita -> Kunci & hp =100340","10. Dompet Wanita -> Lipat =100341","11. Dompet Wanita -> Panjang =100342","12. Dompet Wanita -> Lainnya =100343","13. Tas Wanita Lainnya =100098"]
        btnsimpan = QPushButton('Simpan', self)
        btnsimpan.clicked.connect(self.simpan)

        btnsimpanTop = QPushButton('Simpan', self)
        btnsimpanTop.clicked.connect(self.simpan)
        
        layout.addRow(QLabel(" "), btnsimpanTop)
        layout.addRow(QLabel(" "))
        layout.addRow(QLabel(" "))

        for val in self.dir_list:
            if self.numberx >= int(self.dari) and self.numberx <= int(self.sampai) :
                # print(str(self.numberx)+" - "+str(self.dari)+" - "+str(self.sampai))

                directoryOri = os.getcwd()+"/"+self.pathOri+"/"+val
                # directoryOri = os.getcwd()+"/"+pathOri+"/"+val.split()[1]
                
                batas = QLabel(str(self.numberx))
                batas.setStyleSheet('font-size:50px; text-align:center')
                batas.setAlignment(QtCore.Qt.AlignCenter)

                layout.addRow(batas)
                
                for filename in os.listdir(directoryOri):
                    f = os.path.join(directoryOri, filename)
                    
                    # img = mpimg.imread(self.pathOri+"/"+val+"/"+filename)
                    # imgplot = plt.imshow(img)
                    # plt.show()
                    # img = Image.open(pathOri+"/"+val+"/"+filename)
                    # img.show() untuk windo
                    # print('==========================')
                    self.itemname = []
                    for x, i in enumerate(filename.split()):
                        # print(x, i)
                        self.itemname.append(i)
                    # print('==========================')
                    break

                label = QLabel(' ',self)
                

                self.kode[self.numberx] = QComboBox()
                self.kode[self.numberx].addItems(self.itemname)

                self.harga[self.numberx] = QComboBox()
                self.harga[self.numberx].addItems(self.itemname)

                self.bahan[self.numberx] = QComboBox()
                self.bahan[self.numberx].addItems(self.itemname)
                
                self.bahan2[self.numberx] = QComboBox()
                self.bahan2[self.numberx].addItems(self.itemname)

                self.varian[self.numberx] = QComboBox()
                self.varian[self.numberx].addItems(self.itemname)

                self.size[self.numberx] = QComboBox()
                self.size[self.numberx].addItems(self.itemname)

                self.berat[self.numberx] = QComboBox()
                self.berat[self.numberx].addItems(self.itemname)
                
                self.kategori[self.numberx] = QComboBox()
                self.kategori[self.numberx].addItems(self.itemkategori)

                self.bahantext[self.numberx] = QComboBox()
                self.bahantext[self.numberx].addItems(['pu', 'ox'])

                self.btnm1[self.numberx] = QPushButton('-1')
                self.btnm1[self.numberx].clicked.connect(lambda state, paramid=self.numberx: self.minCurrentIndex(paramid))
                
                self.btnp1[self.numberx] = QPushButton('+1')
                self.btnp1[self.numberx].clicked.connect(lambda state, paramid=self.numberx: self.plusCurrentIndex(paramid))

                self.judul[self.numberx] = QLineEdit(self)
                self.judul[self.numberx].textChanged.connect(lambda state, paramid=self.numberx: self.onchange(paramid))

                url = self.pathOri+"/"+val+"/"+filename
                # for degree and adding combo box
                label.setStyleSheet("border-image:url("+url+") 0 0 0 0 stretch stretch; color:red; border: 1px solid black; height:140px; font-size:190px")
                
                self.harga[self.numberx].setCurrentIndex(self.hargaIndexDefault)
                self.bahan[self.numberx].setCurrentIndex(self.bahanIndexDefault)
                self.bahan2[self.numberx].setCurrentIndex(self.bahan2IndexDefault)
                self.size[self.numberx].setCurrentIndex(self.sizeIndexDefault)
                self.berat[self.numberx].setCurrentIndex(self.beratIndexDefault)
                self.varian[self.numberx].setCurrentIndex(self.varianIndexDefault)

                layout.addRow(QLabel("Gambar"+str(self.numberx)), label)
                layout.addRow(QLabel("Kode"), self.kode[self.numberx])
                layout.addRow(QLabel("Judul"), self.judul[self.numberx])
                layout.addRow(QLabel("Kategori"), self.kategori[self.numberx])
                layout.addRow(QLabel("Harga"), self.harga[self.numberx])
                layout.addRow(QLabel("Bahan"), self.bahan[self.numberx])
                layout.addRow(QLabel("Bahan 2"), self.bahan2[self.numberx])
                layout.addRow(QLabel("Varian"), self.varian[self.numberx])
                layout.addRow(QLabel("Size"), self.size[self.numberx])
                layout.addRow(QLabel("Berat"), self.berat[self.numberx])
                layout.addRow(QLabel("Bahan text"), self.bahantext[self.numberx])
                layout.addRow(QLabel("+ 1"), self.btnp1[self.numberx])
                layout.addRow(QLabel("- 1"), self.btnm1[self.numberx])
                
                layout.addRow(QLabel(" "))
                layout.addRow(QLabel(" "))
                
                layout.addRow(QLabel(" "))
                layout.addRow(QLabel(" "))
            self.numberx += 1

        layout.addRow(btnsimpan)
		
        self.formGroupBox.setLayout(layout)
        scroll = QScrollArea()
        scroll.setWidget(self.formGroupBox)
        scroll.setWidgetResizable(True)

        # setting layout
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        
  
# main method
if __name__ == '__main__':
  
    # create pyqt5 app
    app = QApplication(sys.argv)
  
    # create the instance of our Window
    window = Window()
  
    # showing the window
    window.show()
  
    # start the app
    sys.exit(app.exec())