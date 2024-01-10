"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invetido é {nome invertido}
        Seu nome contem (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba:
        "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome completo: ')
idade = input('Digite sua idade: ')

if nome and idade != "": # Não precisava dessa comparação
    print(f'Seu nome é {nome}')
    print(f'Seu nome invetido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')

    print(f'Seu nome tem {len(nome)} letras (contando espaços)')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
