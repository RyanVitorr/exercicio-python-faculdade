
resposta = 0

classificacao = " "

if resposta == 0:
    pergunta = str(input('Telefonou para a vítima? (S/N) '))
    if pergunta == "S":
        resposta = resposta + 1
    else:
        resposta = resposta
    pergunta = str(input('Esteve no local do crime? (S/N) '))
    if pergunta == "S":
        resposta = resposta + 1
    pergunta = str(input('Mora perto da vítima? (S/N) '))
    if pergunta == "S":
        resposta = resposta + 1
    pergunta = str(input('Devia para a vítima? (S/N) '))
    if pergunta == "S":
        resposta = resposta + 1
    pergunta = str(input('Já trabalhou com a vítima? (S/N) '))
    if pergunta == "S":
        resposta = resposta + 1
  
    

    if resposta == 2:
        classificacao = "Suspeita"
        print(f'{classificacao}')
    elif resposta >= 3 and resposta <= 4:
        classificacao = "Cúmplice"
        print(f'{classificacao}')
    elif resposta == 5:
        classificacao = "Assassino"
        print(f'{classificacao}')
    else:
       print('Inocente')
       