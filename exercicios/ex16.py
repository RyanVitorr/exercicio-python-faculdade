
i = int(input('Informe a sua idade: '))
c = int(input('Informe seu tempo de serviço: '))

if i >= 65:
    print('Você pode se aposentar')
elif c >= 30:
    print('Você pode se aposentar')
elif i >=60 and c >=25:
    print('Você pode se aposentar')
else:
    print('Você não pode se aposentar')