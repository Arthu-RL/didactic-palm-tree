import os
import json

path = 'C:\\Users\\Arthu\\Desktop\\College Projects\\Python Projects\\'
path += 'tasks.json'


def create_file(tasks):
    print("Tasks\n")
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=True, indent=2)
    with open(path, 'r', encoding='utf-8') as file:
        print(*json.load(file), sep='\n')
    print()


def add(t, tasks, save_tasks):
    tasks.append(t)
    save_tasks.insert(0, t)
    return


def tolist(tasks):
    if not tasks:
        print("Tasks\n")
        print("There are no tasks.")
    else:
        create_file(tasks)
    print()


def undo(tasks):
    tasks.pop()
    print("Tasks\n")
    print(*tasks, sep='\n')
    print()


def remake(tasks, save_tasks):
    if len(save_tasks) == 0:
        print("There is nothing to remake.")
        print()
        return

    for n in range(len(tasks)):
        if tasks[n] == None:
            tasks.append(save_tasks[(len(save_tasks) - 1)])
            save_tasks.pop()
            print("Tasks\n")
            print(*tasks, sep='\n')
            print()
            return

    tasks.append(save_tasks[(len(save_tasks)-1)])
    save_tasks.pop()
    print("Tasks\n")
    print(*tasks, sep='\n')
    print()


l1 = []
l2 = []
while True:
    print("Commands: tolist, undo, remake, or save (to end the program, tasks will be saved in the tasks.json file(only if you used tolist command)")
    task = input("Type a task or a command: ")
    print()

    if task == 'save':
        break

    commands = {
        'add': lambda: add(task, l1, l2),
        'undo': lambda: undo(l1),
        'tolist': lambda: tolist(l1),
        'remake': lambda: remake(l1, l2),
        'cls': lambda: os.system('cls')
    }

    command = commands.get(task) if commands.get(task) is not None else commands['add']

    command()
