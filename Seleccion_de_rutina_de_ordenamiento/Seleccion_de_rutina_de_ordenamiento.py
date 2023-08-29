#Gerardo Deústua Hernández- A01736455
#Hugo Muñoz Rodríguez - A01736149
from random import randint
import random
import time

#Declaración de función sort(lista, pivote, ___)
def sort(A, pivote):

    mediana=pivote

    B = A[:len(A)//2]
    C = A[len(A)//2:]

    #Checar si la lista tiene pivote elementos
    if pivote < len(A):   
        if len(B)==len(C):
            index=len(A)//2
            mediana=A[index]
            return mediana
        elif len(B)>A[pivote]:
            mediana = sort(B,pivote)
            return mediana
        elif len(B)<A[pivote]:
            mediana = sort(C,pivote-len(B))
            return mediana
    return mediana

# Lista
input_sizes = list(range(1, 10001, 1000))
my_list = []
for num in input_sizes:
    input_array = list(range(1, num + 1))
    my_list.append(num)
random.shuffle(input_array)
    

pivote=randint(1, len(my_list))
temp1 = time.perf_counter()
mediana = sort(my_list,pivote)
temp2 = time.perf_counter()

#Imprimir resultados
print("Mediana: " + str(mediana) + ".")
print(f"Ejecunción completada en {temp2 - temp1:0.6f} segundos.")

#PUSH de Hugo