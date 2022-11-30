import pandas as pd
import qrcode
b = pd.read_csv ('uniqueID.csv')
# add your own directory instead of one in the code. 
i =0 
for row in b.values: 
    img = qrcode.make(str(row))
    img.save('result/qrcode_test'+'{:0>3}'.format(i)+".png")
    i+=1  


