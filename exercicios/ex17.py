
k = float(input('Quantos Km foi percorrido? '))

l = float(input('Quantos L foi gasto? '))

resultado = k/l

if resultado < 8:
    print(f'Seu carro faz {resultado}km/l, Venda o carro!')
elif resultado >= 8 and resultado <= 14:
    print(f'Seu carro faz {resultado}km/l, seu carro é Econômico!')
else:
    print(f'Seu carro faz {resultado}km/l, seu carro é Super econômico!')