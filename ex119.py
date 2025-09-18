# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


# tarefas = []
# historico = []

# def adicionar(tarefa):
#     tarefa.append(tarefa)
#     historico.append('adicionar', tarefa)

# def desfazer():
#     if not historico:
#         print('Nada para desfazer.')
#         return
    
#     acao, tarefa = historico.pop()
#     if acao == 'adicionar':
#         tarefas.remove(tarefa)
#         print(f"Tarefa '{tarefa}' removida (desfeita).")

# def listar():
#     if not tarefas:
#         print('Nenhuma tarefa na lista.')
#     else:
#         print('\nTarefas atuais:')
#         for i, t in enumerate(tarefas, 1):
#             print(f'{i}. {t}')
#     print()

# def menu():
#     while True:
#         print('=====LISTA DE TAREFAS====')
#         print('1 - Adicionar tarefa')
#         print('2 - Lista tarefas')
#         print('3 - Desfazer última ação')
#         print('4 - Sair')

#         opcao = input('Escolha: ')

#         if opcao == '1':
#             tarefa = input('Digite a tarefa: ')
#             adicionar(tarefa)
#         elif opcao == '2':
#             listar()
#         elif opcao == '3':
#             desfazer()
#         elif opcao == '4':
#             print('Saindo...')
#             break
#         else:
#             print('Opção invalida.\n')

# if __name__ == '__main__':
#     menu()





# tarefas, historico = [], []

# while True:
#     opcao = input("\n[1] Adicionar [2] Listar [3] Desfazer [4] Sair: ")

#     if opcao == "1":
#         t = input("Tarefa: ")
#         tarefas.append(t); historico.append(t)
#     elif opcao == "2":
#         print("Tarefas:", tarefas or "Nenhuma")
#     elif opcao == "3":
#         if historico:
#             t = historico.pop(); tarefas.remove(t)
#             print(f"Desfeito: {t}")
#         else:
#             print("Nada para desfazer.")
#     elif opcao == "4":
#         break
#     else:
#         print("Opção inválida.")


"""
  ===============RESOLUÇÃO DO PROFESSOR=====================
"""


import json
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe, criando novo...')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)


CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer, clear ou sair')
    entrada = input('Digite uma tarefa ou comando: ').strip()

    if entrada == 'sair':
        break

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls' if os.name == 'nt' else 'clear'),
    }

    comando = comandos.get(entrada)

    if comando:
        comando()
    else:
        adicionar(entrada, tarefas)

    salvar(tarefas, CAMINHO_ARQUIVO)

    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'clear':
    #     os.system('clear')
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue