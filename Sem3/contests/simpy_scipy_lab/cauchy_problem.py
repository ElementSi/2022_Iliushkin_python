import scipy as sp
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

continuum = np.linspace(0, 10)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.set_size_inches(8, 8)
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.95,
                    top=0.9,
                    hspace=0.4)

"""
Решение диффура при помощи sympy
"""

x = sym.symbols('x')
y = sym.Function('y')
dydx = y(x).diff(x)
diff_eq = sym.Eq(dydx, - 2 * y(x))

sym_solution = sym.dsolve(diff_eq)

print("\nОбщее решение (sympy):")
print(sym_solution)

sym_solution = sym.dsolve(diff_eq, ics={y(0): 2 ** 0.5})
print("\nРешение задачи Коши (sympy):")
print(sym_solution)

cont_sym_solution = np.empty(0)

for num in continuum:
    cont_sym_solution = np.append(cont_sym_solution, sym_solution.evalf(subs={x: num}).args[1])

ax1.plot(continuum, cont_sym_solution, color='#00D7CF')
ax1.set_title('sympy')

"""
Решение диффура пр помощи scipy
"""


def model(f, t):
    k = 2
    dfdt = - k * f
    return dfdt


cont_sp_solution = sp.integrate.odeint(model, 2 ** 0.5, continuum)
cont_sp_solution = np.reshape(cont_sp_solution, -1)

ax2.plot(continuum, cont_sp_solution, color='#66D700')
ax2.set_title('scipy')

"""
Разница между решениями
"""

ax3.plot(continuum, abs(cont_sp_solution - cont_sym_solution), color='#0700D7')
ax3.set_title('difference')

plt.savefig('diffur_solution.png', dpi=400)
