semana = {"Segunda" : [],"Terça" : [],"Quarta" : [],"Quinta" : [],"Sexta" : [],"Sabado" : [],"Domingo": []}

#print(semana)
while True:
    print('='*13,"Menu", '='*13)
    print("""
    1 - Cadastrar Tarefa
    2 - Excluir Tarefa
    3 - Alterar Tarefa
    4 - Exibir Lista de Tarefas
    0 - Sair
    """)
    print('='*32)
    seletor = int(input("Digite a opção aqui: "))

    match seletor:
        case 1:
            dia_da_semana = input("Digite o dia da semana: ").capitalize().strip()
            tarefa = input("Digite a tarefa: ").strip().capitalize()
            semana[dia_da_semana].append(tarefa)
            print(f"Tarefa cadastrada no dia {dia_da_semana}.")
        case 2:
                escolha = int(input("Deseja deletar algumas dessas tarefas?\n1 - Sim\n0 - Não\nDigite aqui: "))
                if escolha == 1:
                    dia_deletar = input("Digite qual dia você deseja deletar a tarefa: ").capitalize().strip()
                    if dia_deletar in semana:
                        print(f"Tarefas da {dia_deletar.lower()} que podem ser deletadas: ")
                        print(semana[dia_deletar])
                        deletar_tarefa = input("Digite toda a tarefa que você deseja excluir: ").capitalize()
                        if deletar_tarefa in semana[dia_deletar]:
                            semana[dia_deletar].remove(deletar_tarefa)
                            print(semana)

                        


                    
                        
        case 4:
            for dia_da_semana, semana in semana.items():
                print(f"{dia_da_semana}:") 
                for tarefa in semana:
                    print(f" - {semana}")
            
        case 0:
            break    