
p = 0
recebe = 0
valor = 0

while p < 11:
    pergunta = int(input('Digite um número: '))
    valor = valor + pergunta
    p = p + 1
    if p == 10:
        print(f'A soma dos números é: {valor}')
        break

