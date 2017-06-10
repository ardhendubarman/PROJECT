import pickle as pkl
import matplotlib.pyplot as plt
import numpy as np
plt.rc('text', usetex=True)
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

start = False
search_string = "j_o0"
filename = 'tmp.txt'

num_cols = 5
col = []

for i in range(num_cols):
    col.append([])

with open(filename, 'r') as file:
    for line in file:

        if(search_string in line):
            start = True
            del col
            col = []
            for i in range(num_cols):
                col.append([])
            continue

        if(not start):
            continue

        nums = line.split()
        if(len(nums) != num_cols):
            continue
        try:
            for i in range(len(nums)):
                col[i].append(float(nums[i]))
        except:
            pass


x_axis = pkl.load(open('data.pkl', 'rb'))
T = pkl.load(open('temperature.pkl', 'rb'))
conv = col[0]
cond = col[1]
chem = col[2]
diff = col[3]
tdiff = col[4]
#%%
min_y = min(chem)
index = chem.index(min_y)
center = x_axis[1:-1][index]
for i in range(len(x_axis[1:-1])):
    x_axis[i] = (x_axis[i] - center)
##tdiff=[x*(-1) for x in tdiff]
fig, ax1 = plt.subplots()
ax1.set_xlim(-0.0003, 0.0003)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

ax1.plot(x_axis[1:-1], conv,'k--', label='convection')
##ax1.plot(x_axis[1:-1], cond, label= 'conduction')
ax1.plot(x_axis[1:-1], chem,'r-.',label= 'heat realease')
##ax1.plot(x_axis[1:-1], diff,'k', label= 'diffusion')
ax1.plot(x_axis[1:-1], tdiff,'k', label= 'diffusive sum')
plt.legend(frameon=False, handlelength = 3, fontsize=12,loc="upper left",bbox_to_anchor=(0,1))
##plt.legend(frameon=False, handlelength = 3, fontsize=12)
ax2 = ax1.twinx()
ax2.set_xlim(-0.0003, 0.0003)
ax2.plot(x_axis,T,dashes=[8, 4, 2, 4, 2, 4], label= 'Temperature profile')
ax2.set_ylabel('Temperature [K]',fontsize='large')

#flame thickness by Spalding's formula
dy=np.diff(T)
dx=np.diff(x_axis)
i=np.diff(T).argmax()##position of maximum temperature gradient
grad=dy/dx
g=max(grad)
j=grad.argmax()
b=(T[-1]-T[0])/g  #flame_thickness

x1=(T[0]-T[j])/g+x_axis[j]
x2=(T[-1]-T[j])/g+x_axis[j]
theta1=[x1,x2]
ax2.axvline(x1, color='black', lw=0.5, alpha=0.8)#two verical lines will denote flame thickness
ax2.axvline(x2, color='black', lw=0.5, alpha=0.8)

##plot parameters
plt.legend(frameon=False, handlelength = 3, fontsize=12)
ax1.set_ylabel('energy equation terms [$K s^{-1}]$',fontsize='large')##, verticalalignment='center', horizontalalignment ='right'
ax1.set_xlabel('location [m]',fontsize='large')
ax1.minorticks_on()
ax2.minorticks_on()
#ax1.tick_params(axis='x',which='minor',bottom='on')
plt.locator_params(axis='x', nbins=4)
plt.title('298 K - 5 bar', loc='right')

plt.savefig('fig4.pdf',bbox_inches='tight')
plt.show()
