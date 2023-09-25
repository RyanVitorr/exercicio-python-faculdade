
p = 0
recebe = 0
valor = 0

while p < 11:
    pergunta = int(input('Digite um número: '))
    if pergunta > 0:
        valor = valor + pergunta
    else:
        print('Número inválido')
        break
    p = p + 1
    if p == 10:
        print(f'A média dos números é: {valor/10}')
        break
