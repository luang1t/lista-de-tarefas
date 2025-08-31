import os

semana = {"Segunda" : [],"Terça" : [],"Quarta" : [],"Quinta" : [],"Sexta" : [],"Sabado" : [],"Domingo": []}
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
    try:
        seletor = int(input("Digite a opção aqui: "))
    except ValueError:
        os.system('cls')
        print("Opção invalida, digite apenas números. ")
        continue
    match seletor:
        case 1:
            dia_da_semana = input("Digite o dia da semana: ").capitalize().strip()
            if dia_da_semana not in semana:
                print("Dia inválido, digite um dos dias cadastradas.")
                continue
            tarefa = input("Digite a tarefa: ").strip().lower()
            semana[dia_da_semana].append(tarefa)
            print(f"Tarefa cadastrada no dia {dia_da_semana}.")
        case 2:
                for dia_da_semana, tarefas in semana.items():
                    print(f"{dia_da_semana}:") 
                    if tarefas:
                        for indice,tarefa in enumerate(tarefas,start=0):
                            print(f"{indice} - {tarefa}")
                    else:
                        print("Sem tarefas")        
                try:
                    escolha = int(input("Deseja deletar algumas dessas tarefas?\n1 - Sim\n0 - Não\nDigite aqui: "))
                except ValueError:
                        print("Digite apenas 0 ou 1.")   
                        continue
                if escolha == 1:
                    dia_deletar = input("Digite qual dia você deseja deletar a tarefa: ").capitalize().strip()
                    if dia_deletar not in semana:
                        print("Esse dia não existe")
                        continue
                    if not semana[dia_deletar]:
                        print(f"Não há tarefas cadastradas em {dia_deletar}")
                        continue
                    for indice,tarefa in enumerate(semana[dia_deletar],start=0):
                        print(indice,'-',tarefa)
                    try:
                        deletar_tarefa = int(input("Digite o indice da tarefa que você deseja excluir: "))
                    except ValueError:
                        print("Digite apenas numeros!")
                        continue
                            
                    if 0<=deletar_tarefa<len(semana[dia_deletar]):
                        remocao_tarefa = semana[dia_deletar].pop(deletar_tarefa)
                        print(f"Tarefa {remocao_tarefa} removida.")
                    else:
                        print("Número inválido!")             
        case 3:
            dia_update = input("Digite qual dia da semana deseja atualizar a tarefa: ").capitalize().strip()
            if dia_update not in semana:
                print(f"Esse dia {dia_update} não existe!")
                continue
            if not semana[dia_update]:
                print("Não há tarefas cadastradas")
                continue
            for indice, tarefa in enumerate(semana[dia_update], start = 0):
                print(f"{dia_update.capitalize()}")
                print(indice, " - ", tarefa)
            try:
                tarefa_indice = int(input("Digite o número da tarefa que deseja alterar: "))
            except ValueError:
                print("Digite apenas numeros!")
                continue    
                
            if 0<=tarefa_indice<len(semana[dia_update]):
                update_tarefa = input("Digite a nova tarefa: ").strip().lower()
                semana[dia_update][tarefa_indice] = update_tarefa      
            else:
                print("Número inválido")           
        case 4:
            for dia_da_semana, tarefas in semana.items():
                print(f"TAREFAS DE {dia_da_semana.upper()}:") 
                if tarefas:
                    for tarefa in tarefas:
                        print(f" - {tarefa}")
                else:
                    print("Sem tarefas")                  
        case 0:
            break 
        case _:
            print("Opção inexistente, escolha uma do menu.")   