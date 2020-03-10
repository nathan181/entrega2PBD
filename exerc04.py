"""4. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar. O resultado da operação deve ser acompanhado de
uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

n1, n2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))

opcao = input("Qual operação deseja realizar?\n+ - Adição\n- - Subtração\n* - Multiplicação\n/ - Divisão\n")

OK = True

if opcao == "+":
    result = n1+n2
    
elif opcao == "-":
    result = n1-n2

elif opcao == "*":
    result = n1*n2

elif opcao == "/":
    if n2 == 0.0:
        print('Erro! O divisor não pode ser 0.')
        OK = False
    else:
        result = n1/n2
else:
    print('Erro! Opção inválida!')
    OK = False

if not OK:
    pass
else:
    
    r = str(result)
#Testando se o número é inteiro
    if (r[-2]=='.' and r[-1]=='0'):
        conjunto = 'inteiro'
    else:
        conjunto = 'decimal'

#Testando se o número é par (aplica-se apenas a números inteiros)
    if conjunto == 'inteiro':
        if result%2==0:
            parimpar = 'par'
        else:
            parimpar = 'ímpar'   
    else:
        parimpar = 'paridade só se aplica a números inteiros'

#Testando se o número é negativo
    if result < 0.0:
        sinal = 'negativo'
    elif result == 0.0:
        sinal = 'nulo'
    else:
        sinal = 'positivo'

    print(f'Resultado é: {result}, {conjunto}, {sinal}, {parimpar}.')
    
print('Fim de programa.\n')