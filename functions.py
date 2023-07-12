def display_todo(new):
    for idx, item in enumerate(new):
        item = item.title()

        print(f"{idx + 1}) {item}")

def readfile(txt='todos.txt'):
    with open(txt, "r") as file:
        todos = file.readlines()
    return todos

def writefile(new_arg, txt='todos.txt'):
    with open(txt,'w') as file:
        file.writelines(new_arg)