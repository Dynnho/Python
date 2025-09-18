"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontrar_primeiro_duplicado(listas_de_inteiros):
    # for numero in listas_de_inteiros:
    #     print(numero)

    numeros_vistos = set()
    primeiro_duplicado = -1

    for numero in listas_de_inteiros:
        if numero in numeros_vistos:
            primeiro_duplicado = numero
            break
        numeros_vistos.add(numero)
        

    return primeiro_duplicado
   

for lista in lista_de_listas_de_inteiros:
    print(lista, encontrar_primeiro_duplicado(lista))


    """
    def encontrar_primeiro_duplicado(lista_numeros):
       
    Encontra o primeiro número duplicado em uma lista, considerando a segunda ocorrência como a duplicata.

    Args:
        lista_numeros: A lista de números a ser verificada.

    Returns:
        O primeiro número duplicado encontrado, ou -1 se não houver duplicatas.
    
    numeros_vistos = set() # Cria um conjunto para armazenar os números que já foram vistos

    for numero in lista_numeros:
        if numero in numeros_vistos:
            # Se o número já está no conjunto, é uma duplicata
            return numero # Retorna o número duplicado
        numeros_vistos.add(numero) # Adiciona o número ao conjunto

    return -1 # Retorna -1 se nenhum duplicado for encontrado

# Exemplos de uso:
lista1 = [1, 2, 3, 4, 3, 5, 6]
print(f"A lista é: {lista1}")
print(f"O primeiro duplicado é: {encontrar_primeiro_duplicado(lista1)}") # Saída: 3

lista2 = [1, 2, 3, 4, 5, 6]
print(f"A lista é: {lista2}")
print(f"O primeiro duplicado é: {encontrar_primeiro_duplicado(lista2)}") # Saída: -1

lista3 = [10, 20, 30, 20, 10, 40]
print(f"A lista é: {lista3}")
print(f"O primeiro duplicado é: {encontrar_primeiro_duplicado(lista3)}") # Saída: 20

    """