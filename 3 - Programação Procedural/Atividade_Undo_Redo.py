tarefas = []
tarefas_desfeitas = []


def adicionar_tarefa():
    tarefa = input('Informe a tarefa que deseja adicionar: \n')
    tarefas.append(tarefa)
    print('Sua tarefa foi adicionada.')
    print()

    continuar = input('dejesa adicionar outra tarefa ? \n'
                      '1 - sim\n'
                      '2 - não\n'
                      '-> ')

    if continuar == '1':
        adicionar_tarefa()
    elif continuar == '2':
        pass
    else:
        print('Opção inválida!')


def mostra_tarefas():
    for mostra_tarefa in tarefas:
        print(mostra_tarefa)


def undo():
    tarefa_desfeita = tarefas.pop()
    tarefas_desfeitas.append(tarefa_desfeita)


def redo():
    refazer_tarefa = tarefas_desfeitas.pop()
    tarefas.append(refazer_tarefa)


while True:
    qtd_tarefas = len(tarefas)
    qtd_tarefas_desfeitas = len(tarefas_desfeitas)
    op = input('Escolha uma opção: \n'
               '1 - Adicionar uma Tarefa.\n'
               '2 - Ver suas Tarefas.\n'
               '3 - Desfazer Tarefa.\n'
               '4 - Refazer Tarefa.\n'
               '5 - Sair\n'
               '-> ')

    if op == '1':
        adicionar_tarefa()
    elif op == '2':
        if qtd_tarefas == 0:
            print('Você não tem nehuma tarefa adicionada!')
        else:
            print('Suas Tarefas: ')
            mostra_tarefas()
        print()
    elif op == '3':
        if qtd_tarefas == 0:
            print('Você não tem nehuma tarefa adicionada!')
        else:
            undo()
        print()
    elif op == '4':
        if qtd_tarefas_desfeitas == 0:
            print('Você não tem nehuma tarefa adicionada!')
        else:
            redo()
        print()
    elif op == '5':
        break
    else:
        print('Opção inválido!')
        print()
