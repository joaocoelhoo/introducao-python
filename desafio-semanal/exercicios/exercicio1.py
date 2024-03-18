# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

def remove_duplicatas(lista):
    lista_sem_duplicatas = list(set(lista))
    print(lista_sem_duplicatas)


lista_com_duplicatas = [9, 9, 5, 3, 4, 1, 1, 5, 6, 1, 7]
remove_duplicatas(lista_com_duplicatas)
