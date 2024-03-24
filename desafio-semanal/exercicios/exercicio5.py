# Crie um programa que calcule o preço final de um produto após
# aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não:
# - Solicite ao usuário o preço original do produto e o desconto percentual ou
# armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

def calcular_preco(valor_original, desconto):
    desconto_porcento = desconto/100
    valor_com_desconto = valor_original - (valor_original*desconto_porcento)
    return valor_com_desconto


valor_original = float(input("Insira o Valor Original: "))
desconto = float(input("Insira a porcentagem do seu desconto: "))

preco_final = calcular_preco(valor_original, desconto)
print(preco_final)
