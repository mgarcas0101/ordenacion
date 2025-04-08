#Archivo: treselementos.py
#Fecha: 08/04/2025
#proy.: estudio de algoritmos 
#
# Ordenar crecientemente una lista de tres valores
# Existe un error, ya que según los valores, puede cambiar
# dos que entre ellos había que cambiar, perogenera mal orden
# en los dos posteriores. 

n = [252, 14, 58]
def swap(j):
    a = n[j]
    n[j] = n[j+i]
    n[j+i] = a



    for i in range(5):
        for j in range(5):
            if n[j]>n[j+l]:
                swap(j)

print(n)