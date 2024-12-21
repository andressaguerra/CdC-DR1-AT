import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

#vou considerar que uma loja tipo americanas de rua tem preços que variem de R$1,99 até R$ 14 mil
lista_mil = [round(random.uniform(1.99, 14000), 2) for _ in range (1000)]
lista_dez_mil = [round(random.uniform(1.99, 14000), 2) for _ in range (10000)]

inicio_mil = time.time()
bubble_sort(lista_mil.copy())
tempo_mil = time.time() - inicio_mil

inicio_dez_mil = time.time()
bubble_sort(lista_dez_mil.copy())
tempo_dez_mil = time.time() - inicio_dez_mil

print(f"Tempo com mil elementos: {tempo_mil}")
print(f"Tempo com dez mil elementos: {tempo_dez_mil}")