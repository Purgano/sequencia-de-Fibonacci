# functools: módulo do Python que contém ferramentas para funções
# lru_cache: recurso que guarda os resultados de chamadas anteriores de uma função (cache)

from functools import lru_cache

@lru_cache(maxsize=None)
#funções com o calculo finonacci 
def fib_cache(n):
    if n == 0:
        return 0  
    elif n == 1:
        return 1
    else:
        return fib_cache(n-1) + fib_cache(n-2)

# Recebe o número desejado do usuário e verifica se é positivo
# Se for válido, calcula e imprime o termo correspondente da sequência de Fibonacci
try:
    numero_dig = int(input("Digite um número n inteiro positivo: "))

    if numero_dig <= 0:
        print("Erro: digite apenas números inteiros positivos (maiores que zero).")
    else:
        resultado = fib_cache(numero_dig)
        print(f"O {numero_dig} º termo da sequência de Fibonacci é: {resultado}")

except ValueError:
    print("Erro: você precisa digitar um número inteiro válido.")