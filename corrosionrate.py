from corrosiononsetcolumn  import *
from scipy.optimize import curve_fit

def current_density_lin(t, k1, k2):
    return k1 / np.sqrt(t) * 1 / np.sqrt(1 + k2*t)
def current_density_exp(t,b,alpha, c):
    return b*np.exp(-alpha*t)+c

def current_density_ln(t, r, p):
    return p * np.log(r*t)

if timesteps_unin[0] == 0:
    timesteps_unin[0] = 0.00000000000001

def fit_particle(row):
    popt, pcov = curve_fit(current_density_ln, timesteps_unin, row, p0=[0.5, 0.01])
    return popt[0], popt[1] # Return k1 (in A/m*s**0.5) and k2

# Apply the fit_particle function to each row of i_matrix
results = np.apply_along_axis(fit_particle, 1, matrixpercentabs)

# Extract the estimated values of k1 and k2 from the results array
r = results[:, 0]
p = results[:, 1]


print(timesteps_unin)
print('r values:', r)
print('p values:', p)


steps = [i for i in range(1, (len(arrays) + 1), 1)]
# # steps = np.matrix(steps)
# print(np.size(k1_values))
# print(np.size(k2_values))
# print(np.size(steps))

# print(steps)
"""
plt.plot(steps, k1_value, 'g')
plt.savefig(f'unin_S_abs_corr_to_time_10800/plot_k1.png') #change particle type
plt.clf()
plt.plot(steps, k2_value, 'r')
plt.savefig(f'unin_S_abs_corr_to_time_10800/plot_k2.png') #change particle type
"""
'''
plt.plot(steps, k1_value)
plt.plot(steps, k2_value)
plt.show()'''
'''
verify_values = []

alfa = np.matrix(alpha)
beta = np.matrix(b)
gamma = np.matrix(c)


verify_value = current_density(timesteps_unin, beta[:,0], alfa[:,0], gamma[:,0])
verify_value = verify_value.T
plt.plot(timesteps_unin,verify_value)
plt.show()
'''


verify_values = []

a = np.matrix(r)
b = np.matrix(p)


verify_value = current_density_ln(timesteps_unin, a[:,0], b[:,0])
verify_value = verify_value.T
plt.plot(timesteps_unin,verify_value)
plt.ylim(0, 100)
plt.show()

""""
for i in range(len(arrays)):
        plt.plot(timesteps_unin, verify_values[i])
        plt.xlabel('time [s]')
        plt.ylabel('Percetage of pixels crossing the COC [%]')
        plt.ylim(0,110)
        plt.title(label = f'Verification Theta-phase particle {file_list[i]}') #change particle type
        plt.savefig(f'unin_the_A_abs_corr_to_time_10800/plot_{file_list[i]}_verification.png') #change particle type
        plt.clf()"""