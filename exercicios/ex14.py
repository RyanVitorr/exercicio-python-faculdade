
n1 = float(input('Nota do trabalho de laboratório: '))

n2 = float(input('Nota da avaliação semestral: '))

n3 = float(input('Nota do exame final: '))

if (n1 >= 0 and n1 <=10) and (n2 >= 0 and n2 <=10) and (n3 >= 0 and n3 <=10):
    media = (n1 * 2) + (n2 * 3) + (n3 * 5)/10
    if media >= 0 and media <= 2.9:
        print(f'Sua média é; {media}, você está reprovado.')
    elif media >= 3 and media <= 4.9:
        print(f'Sua média é; {media}, você está de recuperação')
    else:
        print(f'Sua média é; {media}, você foi aprovado.')
else:
    print('Alguma nota está errada.')