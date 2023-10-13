import pandas as pd
import requests
import time
import qrcode
import re
import csv
import os
import shutil

file = 'output/'

excel_data_df = pd.read_excel("Neshi.xlsx", sheet_name='sheet1')
data = excel_data_df['tot'].tolist()

for new in data:
    nams = str(new)
    ddnname = nams.split("DDN:",1)[1]
    #filename =ddnname.split('LONGITUDE')[0]
    qr = qrcode.QRCode(version = 1,
                     box_size = 10,
                     border = 1)
    qr.add_data(nams)
    qr.make(fit = True)
    img = qr.make_image()
    img.save(ddnname +'.png')
   #time.sleep(1)
 
