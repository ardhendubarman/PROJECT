import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
x_axis = pkl.load(open('data.pkl', 'rb'))
T = pkl.load(open('temperature.pkl', 'rb'))
##print (T)
##x = np.array(T, dtype=np.float)
dy=np.diff(T)
dx=np.diff(x_axis)
i=np.diff(T).argmax()
##print (i)
##print ('max dy %f' %dy[i])
##print ('dx %f' %dx[i])
grad=dy/dx
g=max(grad)
j=grad.argmax()
print(j)
##max_grad=dy[i]/dx[i]
##print (max_grad)
b=(T[-1]-T[0])/g #flame_thickness
####print ('max grad %f' %max_grad)
##print ('flame thickness is %f' %b)

fig, ax2 = plt.subplots()
##ax2.set_xlim(-0.0003, 0.0003)
##ax.axhline(theta, color='green', lw=2, alpha=0.5)
ax2.plot(x_axis,T,dashes=[8, 4, 2, 4, 2, 4], label= 'Temperature profile')
ax2.set_ylabel('Temperature [K]',fontsize='large')
x1=(T[0]-T[j])/g+x_axis[j]
x2=(T[-1]-T[j])/g+x_axis[j]
##ax1.plot(r.date, r.close, lw=2)
theta=[x1,x2]
##ax2.fill_between(theta, 298, T[-1], facecolor='blue', alpha=0.5)
ax2.axvline(x1, color='black', lw=0.5, alpha=0.8)
ax2.axvline(x2, color='black', lw=0.5, alpha=0.8)
plt.show()

