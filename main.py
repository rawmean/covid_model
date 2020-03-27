import matplotlib.pyplot as plt

a = 0.3   # each person can infect (1 + a) person who has not gotten the virus already
a2 = 0.2

N = 1
N2 = 1

Nmax = 3.3e6 * 0.5   # assuming only 50% of people in San Diego will get it

time_array = []
r_array = []
r2_array = []
N_array = []
N2_array = []

t = 0
dt = 0.01
N0 = 1
while t < 120:
    Nold = N
    N2old = N2
    N = N + a * (1 - N / Nmax) * N * dt
    r = (N - Nold) / dt
    N2 = N2 + a2 * (1 - N2 / Nmax) * N2 * dt
    r2 = (N2 - N2old) / dt

    t = t + dt
    time_array.append(t)
    r_array.append(r)
    r2_array.append(r2)
    N_array.append(N)
    N2_array.append(N2)


plt.figure(1)

plt.plot(time_array, r_array)
plt.plot(time_array, r2_array)
plt.xlabel('days after first infection')
plt.ylabel(f'new daily infections')
plt.legend((f'infection rate = {a}', f'infection rate = {a2}'))

plt.figure(2)
plt.plot(time_array, N_array)
plt.plot(time_array, N2_array)
plt.xlabel('days after first infection')
plt.ylabel(f'total # of  infections')
plt.legend((f'infection rate = {a}', f'infection rate = {a2}'))

plt.show()
