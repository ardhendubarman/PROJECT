import matplotlib
import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
plt.rc('text', usetex=True)
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
##x = pkl.load(open('temp.pkl', 'rb'))
x = np.linspace(300, 1400, 30)
x2 = np.linspace(300, 1400, 31)
x3 = np.linspace(300, 1350, 30)
np.put(x3,18,920)
y1 = pkl.load(open('vel_0.32.pkl', 'rb'))
y2 = pkl.load(open('vel_0.34.pkl', 'rb'))
y3 = pkl.load(open('vel_0.38.pkl', 'rb'))
y4 = pkl.load(open('vel_0.46.pkl', 'rb'))
y5 = pkl.load(open('vel_0.62.pkl', 'rb'))
y6 = pkl.load(open('vel_0.94.pkl', 'rb'))
y7 = pkl.load(open('vel_1.58.pkl', 'rb'))
y1 = [x * 100 for x in y1]
y2 = [x * 100 for x in y2]
y3 = [x * 100 for x in y3]
y4 = [x * 100 for x in y4]
y5 = [x * 100 for x in y5]
y6 = [x * 100 for x in y6]
y7 = [x * 100 for x in y7]
#%%


import csv

with open( 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(y1)
