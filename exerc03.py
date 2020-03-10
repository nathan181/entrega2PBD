"""3. Faça um Programa que peça um número correspondente a um determinado
ano e em seguida informe se este ano é ou não bissexto."""

ano = int(input("Forneça o ano: "))


"""if ano%400==0:
    isBissexto = True
elif ano%100!=0 and ano%4==0:
    isBissexto = True
else:
    isBissexto = False"""


if ano%400==0 or ano%100!=0 and ano%4==0:
    isBissexto = True
else:
    isBissexto = False

print(f'O ano {ano} é bissexto' if isBissexto else f'O ano {ano} não é bissexto')