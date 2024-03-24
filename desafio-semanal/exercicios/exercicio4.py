# Crie um programa que conte quantas vezes cada tipo de
# fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não:
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do
# dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.


def contagem_de_frutas(lista_de_frutas):
    contagem = {}
    for fruta in lista_de_frutas:
        contagem[fruta] = contagem.get(fruta, 0) + 1
    return contagem


frutos = [
    "Banana", "Melancia", "Pitomba", "Cajá", 
    "Goiaba", "Pitomba", "Cajá", "Banana", "Manga"
    ]

contagem = contagem_de_frutas(frutos)
print(contagem)
