# To-do List - App de Lista de Tarefas

Boas vindas à documentação do repositório **To-do List**. Esta é uma aplicação de lista de tarefas simples criada usando a biblioteca Tkinter em Python.

## Visão Geral

Este repositório contém o código-fonte da aplicação To-do List. A aplicação permite que os usuários adicionem e removam tarefas de uma lista de tarefas usando uma interface gráfica simples.

## Funcionalidades

- Adicionar tarefas à lista.
- Remover tarefas da lista.
- Exibir a lista de tarefas atualizada em uma interface gráfica.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Além disso, é necessário ter a biblioteca Tkinter, que geralmente é incluída na instalação padrão do Python.

## Instalação

1. Clone este repositório em sua máquina local:

```bash
git clone https://github.com/Gabbyroba/To-do-list.git
```

2. Navegue até o diretório do projeto:

```bash
cd To-do-list
```

3. Execute o arquivo `main2.py`:

```bash
python main2.py
```

## Uso

1. Após executar o comando acima, a interface gráfica da aplicação será aberta.
2. Digite uma tarefa na caixa de entrada de texto e clique no botão "Add Task" para adicioná-la à lista.
3. Para remover uma tarefa, selecione-a na lista e clique no botão "Delete Task".
4. A lista de tarefas atualizada será exibida na caixa de listagem.

## Exemplo de Código

```python
from tkinter import *

root = Tk()
root.title("To-Do List")

tasks = []

def add_task():
    task = task_entry.get()
    tasks.append(task)
    update_listbox()

def delete_task():
    task = listbox.get(ANCHOR)
    tasks.remove(task)
    update_listbox()

def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

task_entry = Entry(root, width=30)
task_entry.pack(pady=10)

add_button = Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

listbox = Listbox(root, width=50)
listbox.pack()

root.mainloop()
```

## Contribuição

Se você gostaria de contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request para discutir suas ideias ou sugestões.
