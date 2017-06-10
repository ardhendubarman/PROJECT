"""
A freely-propagating, premixed hydrogen flat flame with multicomponent
transport properties.
"""

import cantera as ct
import pickle as pkl
import numpy as np
# Simulation parameters
p = 5*ct.one_atm  # pressure [Pa]
Tin = 600.0  # unburned gas temperature [K]
reactants = 'CH4:1, O2:2, N2:7.52'  # premixed gas composition

initial_grid = np.linspace(0.0, 0.32, 7)  # m
tol_ss = [1.0e-5, 1.0e-13]  # [rtol atol] for steady-state problem
tol_ts = [1.0e-4, 1.0e-13]  # [rtol atol] for time stepping
loglevel = 1  # amount of diagnostic output (0 to 8)
refine_grid = True  # 'True' to enable refinement, 'False' to disable

# IdealGasMix object used to compute mixture properties
gas = ct.Solution('gri30.xml')
gas.TPX = Tin, p, reactants

# Flame object
f = ct.FreeFlame(gas, initial_grid)
f.flame.set_steady_tolerances(default=tol_ss)
f.flame.set_transient_tolerances(default=tol_ts)

# Set properties of the upstream fuel-air mixture
f.inlet.T = Tin
f.inlet.X = reactants

#f.show_solution()

# Solve with the energy equation disabled
f.energy_enabled = False
f.set_max_jac_age(20, 20)
f.set_time_step(1e-5, [2, 5, 10, 20])
f.solve(loglevel=loglevel, refine_grid=False)
##f.save('adiabatic.xml', 'no_energy', 'solution with the energy equation disabled')

# Solve with the energy equation enabled
f.transport_model= 'Mix'
f.set_refine_criteria(ratio=3, slope=0.1, curve=0.3)
f.energy_enabled = True
f.solve(loglevel=loglevel, refine_grid=refine_grid)
f.save('adiabatic.xml', 'energy', 'solution with mixture-averaged transport')
#f.show_solution()
print('mixture-averaged flamespeed = {0:7f} m/s'.format(f.u[0]))

# Solve with multi-component transport properties
# f.transport_model = 'Multi'
# f.solve(loglevel, refine_grid)
# f.show_solution()
# print('multicomponent flamespeed = {0:7f} m/s'.format(f.u[0]))
# f.save('h2_adiabatic.xml','energy_multi',
#        'solution with multicomponent transport')

# write the velocity, temperature, density, and mole fractions to a CSV file
#f.write_csv('adiabatic.csv', quiet=True)


##%
index1=gas.species_index('CH4')
index2=gas.species_index('CH2O')
index3=gas.species_index('HCO')
index4=gas.species_index('CO')
z=f.grid

import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

index=np.argmax(f.X[index4])
center = z[index]
for k in range(len(z)):
    z[k] = (z[k] - center)

plt.figure(figsize=(3.75,7.5))
plt.xlim(-0.0005, 0.0005)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.plot(z,f.X[index1],dashes=[8, 4, 2, 4, 2, 4],label='$X_{CH_4}$')
plt.plot(z,20*f.X[index2],'r-.',label='$X_{CH_2O}*20$')
plt.plot(z,600*f.X[index3],label='$X_{HCO}*600$')
plt.plot(z,f.X[index4],'k--',label='$X_{CO}$')
plt.legend(frameon=True, handlelength = 3, fontsize=12)
plt.ylabel('Mole fractions',fontsize='large')
plt.xlabel('location [m]',fontsize='large')
plt.locator_params(axis='x', nbins=2)
plt.minorticks_on()
fig = plt.figure(1)
ax = fig.add_subplot(111)
t = ax.xaxis.get_offset_text()
t.set_size(18)
plt.title('600 K', loc='right')
plt.savefig('fig6_600.pdf',bbox_inches='tight')
plt.show()
