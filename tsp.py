import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt

X = [0,2,5,6,8]
Y = [2,5,2,6,3]
n=len(X)

M = np.zeros([n,n])
for i in np.arange(0,n,1):
    for j in np.arange(0,n,1):
        if i!=j:
            M[i,j]=sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2)
        else:
            M[i,j]=float('inf')

way=[0, ]

for i in np.arange(1,n,1):
    s=[]
    for j in np.arange(0,n,1):
        s.append(M[way[i-1],j])
    way.append(s.index(min(s)))
    for j in np.arange(0,i,1):
        M[way[i],way[j]]=float('inf')

print("Порядок посещения точек: ", way)

distance = 0
for i in way:
    try:
        print(f'{X[i], Y[i]} -> {X[way[way.index(i)+1]], Y[way[way.index(i)+1]]}')
        distance += sqrt((X[i]-X[way[way.index(i)+1]])**2+(Y[i]-Y[way[way.index(i)+1]])**2)
        print(distance)
    except:
        print(f'{X[i], Y[i]} -> {X[0], Y[0]}')
        distance += sqrt((X[way[n-1]]-X[way[0]])**2+(Y[way[n-1]]-Y[way[0]])**2)
        print(distance)

print("Итоговый путь: ", distance)

X1=[X[way[i]] for i in np.arange(0,n,1)]
Y1=[Y[way[i]] for i in np.arange(0,n,1)]
plt.title('Стартовая точка: %s. Координаты: %s. Общий путь: %s.'%(0, (X[0], Y[0]),round(distance,3)), size=14)
plt.plot(X1, Y1, color='r', linestyle=' ', marker='o')
plt.plot(X1, Y1, color='b', linewidth=1)
X2=[X[way[n-1]],X[way[0]]]
Y2=[Y[way[n-1]],Y[way[0]]]
plt.plot(X2, Y2, color='g', linewidth=2,  linestyle='--', label='Путь от  последнего \n к первому городу')
plt.legend(loc='best')
plt.grid(True)
plt.show()