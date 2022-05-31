import os

directoryOri = 'F:\Shopee\CenterYourFashion\KATALOG_SEMUA_TAS_ORINAME\B0023'
countVarians = len([name for name in os.listdir(directoryOri) if os.path.isfile(os.path.join(directoryOri, name))])
print(countVarians)
