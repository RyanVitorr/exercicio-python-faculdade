
a = float(input('Digite sua altura: '))
s = str(input('Informe seu sexo, digite M mara masculino e F para feminino.  '))

if s == "M" and a > 0:
    print(f'Seu peso ideal é: {(72.7 * a) - 58}')
elif s == 'F' and a > 0:
    print(f'Seu peso ideal é: {(62,1 * a) - 44,7}')
else:
    print('Alguma informação está errada')