
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

if (n1 >= 0 and n1 <=10) and (n2 >= 0 and n2 <=10):
    print(f'Sua média é de {(n1 + n2)/2 }')
else:
    print('Notas informadas invalidas!')