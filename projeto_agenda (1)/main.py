import back

def menu():
    while True:
        print("\nAgenda de Contatos")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Editar contato")
        print("5 - Apagar contato")
        print("6 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            back.adicionar(nome, telefone)
            print("Contato adicionado!")
        elif opc == '2':
            contatos = back.listar()
            if contatos:
                for i, c in enumerate(contatos, 1):
                    print(f"{i}. {c['nome']} - {c['telefone']}")
            else:
                print("Nenhum contato cadastrado.")
        elif opc == '3':
            termo = input("Buscar por nome: ")
            resultados = back.buscar(termo)
            if resultados:
                for c in resultados:
                    print(f"{c['nome']} - {c['telefone']}")
            else:
                print("Nenhum contato encontrado.")
        elif opc == '4':
            contatos = back.listar()
            if contatos:
                for i, c in enumerate(contatos, 1):
                    print(f"{i}. {c['nome']} - {c['telefone']}")
                try:
                    idx = int(input("Número do contato para editar: ")) - 1
                    nome = input("Novo nome: ")
                    telefone = input("Novo telefone: ")
                    if back.editar(idx, nome, telefone):
                        print("Contato atualizado!")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada inválida.")
            else:
                print("Nenhum contato cadastrado.")
        elif opc == '5':
            contatos = back.listar()
            if contatos:
                for i, c in enumerate(contatos, 1):
                    print(f"{i}. {c['nome']} - {c['telefone']}")
                try:
                    idx = int(input("Número do contato para apagar: ")) - 1
                    if back.apagar(idx):
                        print("Contato apagado!")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada inválida.")
            else:
                print("Nenhum contato cadastrado.")
        elif opc == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
