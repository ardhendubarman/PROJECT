import pickle as pkl
import numpy as np
y1 = pkl.load(open('vel_0.32.pkl', 'rb'))
y2 = pkl.load(open('vel_0.34.pkl', 'rb'))
y3 = pkl.load(open('vel_0.38.pkl', 'rb'))
y4 = pkl.load(open('vel_0.46.pkl', 'rb'))
y1 = [x * 100 for x in y1]
y2 = [x * 100 for x in y2]
y3 = [x * 100 for x in y3]
y4 = [x * 100 for x in y4]
x = np.linspace(300, 1400, 30)
da=[]
for i in range (1,30):
    da.append([x[i],y1[i],y2[i],y3[i],y4[i],])

import csv
with open('outputdata.csv', 'w') as outfile:
    mywriter = csv.writer(outfile)
    # manually add header
    mywriter.writerow(['Grid=0.32', ' ','Grid=0.34', 'Grid=0.38', 'Grid=0.46', ' '])
    mywriter.writerow(['Temperature', 'S_l', 'S_l', 'S_l', 'S_l'])
    for d in da:
        mywriter.writerow(d)
