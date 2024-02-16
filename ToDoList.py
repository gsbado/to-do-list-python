'''Funcionalidades Básicas:

1. Adicionar Tarefa:
Permitir que o usuário adicione uma nova tarefa à lista.
Solicitar ao usuário a descrição da tarefa.

2. Visualizar Lista de Tarefas:
Permitir que o usuário visualize a lista de tarefas existentes no arquivo.
Exibir cada tarefa numerada.

3. Marcar Tarefa como Concluída:
Permitir que o usuário marque uma tarefa como concluída.
Solicitar o número da tarefa que deve ser marcada como concluída.
Atualizar a visualização das tarefas

4. Remover Tarefa
Permita ao usuário remover uma tarefa da lista'''


tarefas = []

def adicionar_tarefa(tarefas):
    resposta = 'S'
    while resposta == 'S':
        tarefa = input('Digite a descrição da sua tarefa: ')
        tarefas.append(tarefa)
        print(f'Tarefa "{tarefa}" adicionada com sucesso! Total de tarefas: {len(tarefas)}')
        resposta = input('\nDeseja adicionar outra tarefa? (S/N): ').upper()
    
def listar_tarefas():
    print(f'Total de tarefas: {len(tarefas)}')
    for indice, tarefa in enumerate (tarefas, start=1):
        status = '' if '[CONCLUÍDA]' in tarefa else ' [PENDENTE]'
        print(f'{indice}. {status} {tarefa}')

def concluir_tarefa(tarefas):
    listar_tarefas()
    tarefa_concluida = int(input("Digite o número da tarefa a ser marcada como concluída: "))
    if 1 <= tarefa_concluida <= len(tarefas):
        tarefas[tarefa_concluida - 1] = '[CONCLUÍDA] ' + tarefas[tarefa_concluida - 1]
        print ("Tarefa marcada como concluída com sucesso!")
    else:
        print("Número de tarefa inválido.")

def remover_tarefa():
    listar_tarefas()
    tarefa_removida = int(input("Digite o número da tarefa a ser removida da lista: "))
    if tarefa_removida <= len(tarefas):
        tarefas.pop(tarefa_removida - 1)
        print ("Tarefa removida com sucesso!")
    else:
        print("Número de tarefa inválido.")

# Loop principal
while True:
    print('\n***GERENCIADOR DE TAREFAS***')
    print('\nBem-vindo ao gerenciador de tarefas!')
    print('1. Adicionar Tarefa')
    print('2. Listar Tarefas')
    print('3. Concluir Tarefa')
    print('4. Remover Tarefa')
    print('5. Sair')

    opcao = input('\nDigite o número da opção desejada: ')

    if opcao == '1':
        print('\nVocê escolheu: adicionar uma tarefa')
        adicionar_tarefa(tarefas)
    
    elif opcao == '2':
        print('\nVocê escolheu: listar as tarefas')
        listar_tarefas()
    
    elif opcao == '3':
        print('\nVocê escolheu: concluir uma tarefa')
        concluir_tarefa(tarefas)
    
    elif opcao == '4':
        print('\nVocê escolheu: remover uma tarefa')
        remover_tarefa()

    elif opcao == '5':
        print('Saindo do gerenciador...')
        break
    
    else:
        print('Erro: opção inválida. Por favor, digite uma opção entre 1 e 5.')