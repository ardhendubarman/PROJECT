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
dy=np.diff(y5)
dx=np.diff(x2)
i=np.diff(y5).argmax()
grad=dy/dx
g=max(grad)
j=grad.argmax()
#%%
fig1, ax1 = plt.subplots()
ax1.loglog(x,y1,'k-o',label='$\Delta$X=0.32 m')
ax1.loglog(x,y2,'k-v',label='$\Delta$X=0.34 m')
ax1.loglog(x,y3,'k',label='$\Delta$X=0.38 m')
ax1.loglog(x,y4,'k-s',label='$\Delta$X=0.46 m')
ax1.loglog(x2,y5,'kx',label='$\Delta$X=0.62 m')
ax1.loglog(x3,y6,'k*',label='$\Delta$X=0.94 m')
ax1.loglog(x3,y7,'k-d',label='$\Delta$X=1.58 m')
ax1.axvline(x[j-5], color='black',linestyle='--', lw=1.8, alpha=1)
ax1.set_xlim(200,1900)
ax1.set_ylim(0,1500)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xticks([300,500, 1000, 1500])
ax1.minorticks_on()
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.set_xlabel('preheating temperature [K]')
ax1.set_ylabel("velocity of the incoming mixture $10^{-2}$[$m s^{-1}$]",fontsize=16)
plt.title('$\phi$=1; p = 1bar', loc = "right")
plt.legend(frameon='True', loc='best')
plt.grid(True)
# plt.locator_params(axis='x', nbins=4)
plt.savefig('fig7b.pdf', bbox_inches='tight')
plt.show()
