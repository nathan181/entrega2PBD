"""6. O Hipermercado Tabajara está com uma promoção de carnes que é
imperdível. Confira: 
             Até 5 Kg               Acima de 5 Kg
File Duplo   R$ 4,90 por Kg        R$ 5,80 por Kg
Alcatra      R$ 5,90 por Kg        R$ 6,80 por Kg
Picanha      R$ 6,90 por Kg        R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne por
cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e
a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo
as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar."""

tipo_carne = int(input("Informe o tipo de carne:\n1 - Filé duplo\n2 - Alcatra\n3 - Picanha\n"))
qtd_carne = float(input("Informe a quantidade (em KG) de carne comprada: "))
tipo_pagto = int(input("Informe o tipo de pagamento:\n1 - Dinheiro\n2 - Cartão\n"))
desconto = 0.0

if tipo_carne == 1:
    tipo_carne = 'Filé duplo'
    if qtd_carne <= 5.0:
        total = qtd_carne*4.9
    else:
        total = qtd_carne*5.8

elif tipo_carne == 2:
    tipo_carne = 'Alcatra'
    if qtd_carne <= 5.0:
        total = qtd_carne*5.9
    else:
        total = qtd_carne*6.8

else:
    tipo_carne = 'Picanha'
    if qtd_carne <= 5.0:
        total = qtd_carne*6.9
    else:
        total = qtd_carne*7.8

if(tipo_pagto == 1):
    tipo_pagto = 'Dinheiro'
else:
    tipo_pagto = 'Cartão'
    desconto = 0.05 * total

total_final = total - desconto
    
print(f'Tipo de carne: {tipo_carne}\nQuantidade comprada: {qtd_carne}\nPreço total: {total}\nTipo de pagamento: {tipo_pagto}\nValor do desconto: {desconto}\nTotal a pagar: {total_final}')