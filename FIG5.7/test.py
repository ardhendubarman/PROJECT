import matplotlib
from matplotlib import pyplot as plt
import pickle as pkl
import numpy as np
plt.rc('text', usetex=True)
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
x5 = np.linspace(300,1500,20)
y5 = pkl.load(open('del_0.62.pkl', 'rb'))
##y5 = [np.log(x) for x in y5]
##x5 = [np.log(x) for x in x5]
xl= x5[-2:]
yl= y5[-2:]
##print(xl,yl)
y=[]
m=(yl[1]-yl[0])/(xl[1]-xl[0])
for i in range(0,19):
    y_1=m*(x5[i]-xl[0])+yl[0]
    y.append(y_1)
##    print(x5[i],y[i],'\n')

##print(x5,y,'\n')
fig1, ax1 = plt.subplots()
ax1.plot(x5[:-1],y,'k-o',label='$\Delta$X=0.32 m')
ax1.set_xlim(500,1600)
ax1.set_ylim(0.001,5)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xticks([500, 1000, 1500])
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.set_xlabel('preheating temperature [K]',fontsize=16,fontweight='bold')
ax1.set_ylabel("time from inlet to \ntemperature inflection point[s]",multialignment='center',fontsize=16)
plt.title('$\phi$=1; p = 1bar', loc = "right")
plt.legend(frameon='True', loc='best')
plt.grid('on')
# plt.locator_params(axis='x', nbins=4)
##plt.savefig('fig12.pdf', bbox_inches='tight')
plt.show()
