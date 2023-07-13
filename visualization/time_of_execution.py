import time
import matplotlib.pyplot as plt
from math import factorial



n_vertices = 12

#criar lista de tempos
y_list = []
i = 0

for c in range(0,n_vertices+1):
    tic = time.process_time()
    
    for d in range(0,factorial(c)):
        i +=1
    toc = time.process_time()
    
    y_list.append(toc-tic)

#criar lista de numero de vértices
x_list = []
for c in range(0,n_vertices+1):
    x_list.append(c)

print(x_list)
print(y_list)
plt.plot(x_list, y_list, marker= 'o')
plt.xlabel("Número de vértices")
plt.ylabel("Tempo de execução(s)")
plt.title("Tempo de execução do algoritmo de força bruta")
plt.grid(which='both')
plt.show()



