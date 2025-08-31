import os
def clear():
    os.system('cls')
def menu():
    return print(""" =========MENU===========
| 1 - CADASTRAR TAREFAS  |
| 2 - MOSTRAR TAREFAS    |
| 3 - EDITAR TAREFAS     |
| 4 - DELETAR TAREFAS    |
| 0 - FINALIZAR PROGRAMA |          
 ========================
""")
def recebe_dia(semana):
    while True:
            dia = input("Digite o dia da semana correspondente:\nSegunda,Terça,Quarta,Quinta,Sexta,Sabado,Domingo\nDigite aqui: ").capitalize().strip()
            if dia in semana:
                return dia
            else:
                print("Dia invalido, tente novamente!")

            """
            FUNÇÃO: recebe_dia

            RESPONSABILIDADE:
            Receber do usuário o nome de um dia da semana e validar se esse dia existe no dicionário 'semana'.

            PARÂMETROS:
            - semana(dict): referência para dicionário já existente na memória, usado para validar os dias.

            FUNCIONAMENTO:
            1.Solicita do usuário um input com o nome do dia da semana.
            2.Normaliza a entranda utilizando '.capitalize()' e 'strip()' para evitar erros de digitação comuns.
            3.Verifica se o dia informado existe como chave no dicionario 'semana'.
                -Caso exista, retorna o dia.
                -Caso contrário, informa o erro e pede novamente a entrada.

            RETORNO:
            -(str): O nome válido de um dia da semana presente no dicionário.
            """                
def mostrar_lista(semana):
    for dia_da_semana, tarefas in semana.items():
        print({dia_da_semana})
        if tarefas:
            for indice,tarefas in enumerate(tarefas,start=0):
                print(f"{indice+1} - {tarefas}")
        else:
            print("Sem tarefas")    


semana = {"Segunda" : [],"Terça" : [],"Quarta" : [],"Quinta" : [],"Sexta" : [],"Sabado" : [],"Domingo": []}
while True:
    menu()
    try:
        seletor = int(input("Digite a opção aqui: "))
    except ValueError:
        clear()
        print("Digite algo no contexto do programa.")
    match seletor:
        case 1:
            tarefa = input("Digite a nova tarefa: ")
            semana[recebe_dia(semana)].append(tarefa)
            print("Tarefa registrada!")
        case 2:
            mostrar_lista(semana)
            