import numpy as np

arregloA = np.random.randint (500 , size = 100)
print(arregloA)

print(arregloA [0::2])

print (arregloA.max())



print (arregloA.min())

arregloB = arregloA

print(arregloB * 3) 

print(arregloB.sum())

print(arregloB.mean())

#for i in range (arregloA):
  #if i == 2 % = 0:
    #cont_par = cont_par + 1 
    #print(cont_par)
print(arregloB % 2  == 0)