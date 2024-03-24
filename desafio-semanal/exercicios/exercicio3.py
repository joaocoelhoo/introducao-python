# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não:
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a
# ordenação seja case-insensitive.


def ordernacao_frutas(lista_com_frutas):
    lista_com_frutas.sort(key=str.lower)
    return lista_com_frutas


lista = ["mamao", "Caju", "Uva", "melancia", "Banana"]


frutas_ordenadas = ordernacao_frutas(lista)

print(frutas_ordenadas)
