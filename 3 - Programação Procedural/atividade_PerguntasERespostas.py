quetoes = {
    'Primeira pergunta' : {
        'Pergunta' : 'Quem foi a primeira pessoa a viajar no Espaço?',
        'Alternativas' : {'a': 'Yuri Gagarin', 'b' : 'A cadela Laika', 'c' : 'Neil Armstrong', 'd' : 'Marcos Pontes'},
        'Resposta' : 'a',
    },
    'Segunda pergunta' : {
        'Pergunta' : 'Qual a montanha mais alta do mundo?',
        'Alternativas' : {'a': 'Mauna Kea', 'b' : 'Dhaulagiri', 'c' : 'Monte Chimborazo', 'd' : 'Monte Everest'},
        'Resposta' : 'd',
    },
    'Terceira pergunta' : {
        'Pergunta' : 'Onde se localiza Machu Picchu?',
        'Alternativas' : {'a': 'Colômbia', 'b' : 'Peru', 'c' : 'China', 'd' : 'Bolívia'},
        'Resposta' : 'b',
    },
}
qntd_acertos = 0
for k_pergunta, v_pergunta in quetoes.items():
    print(f'{k_pergunta}: {v_pergunta["Pergunta"]}')

    for k_alternativa, v_alternativa in v_pergunta['Alternativas'].items():
        print(f'{k_alternativa}) {v_alternativa}')

    resposta = input('Informe a alternativa correta: ')
    if resposta == v_pergunta['Resposta']:
        print(f'Parabéns! Você acertou! :)')
        qntd_acertos += 1
    else:
        print(f'Você errou! :( alternativa certa é: letra {v_pergunta["Resposta"]}')
    print()

qntd_questoes = len(quetoes)
porcentagem_acertos = qntd_acertos / qntd_questoes * 100
print(f'Você acertou {porcentagem_acertos:.1f}% das questões.')
