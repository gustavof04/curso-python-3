import os
import platform
import json
# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

todo = []
undo = []
redo = []

while True:
    options = input('Comandos: listar, desfazer, refazer, sair\nDigite uma tarefa ou comando: ')
    
    if options == 'listar':
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        print()
        print('SUAS TAREFAS ATUAIS SÃO:')
        for task in todo:
            print(task)
        print()
        with open('tasks.json', 'w') as f:
            json.dump(todo, f)
    elif options == 'desfazer':
        if len(todo) == 0:
            print('Nada a desfazer')
        else:
            undone_task = todo.pop()
            undo.append(undone_task)
            if platform.system() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')
            print()
            print(f'Tarefa {undone_task} desfeita com sucesso!')
            print('TAREFAS:', *todo, sep='\n')
            print()
            with open('tasks.json', 'w') as f:
                json.dump(todo, f)
    elif options == 'refazer':
        if len(undo) == 0:
            print('Nada a refazer')
        else:
            redone_task = undo.pop()
            todo.append(redone_task)
            redo.append(redone_task)
            if platform.system() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')
            print()
            print(f'Tarefa {redone_task} refeita com sucesso!')
            print('TAREFAS:', *todo, sep='\n')
            print()
            with open('tasks.json', 'w') as f:
                json.dump(todo, f)
    else:
        todo.append(options)
        redo.clear
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        print()
        print('TAREFAS:', *todo, sep='\n')
        print()
        with open('tasks.json', 'w') as f:
                json.dump(todo, f)
    if options == 'sair':
        os.remove('tasks.json')
        break
