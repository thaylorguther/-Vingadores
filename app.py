from interface import Interface
from vingador import Vingador

def inicializar_vingadores():
    # Pré-cadastro de alguns vingadores para facilitar os testes
    Vingador("Thor", "Thor Odinson", "Deidade", ["Martelo", "Força sobre-humana"], "Força sobre-humana", ["Destruição de objetos", "Fogo"], 10000)
    Vingador("Capitão América", "Steve Rogers", "Humano", ["Força aumentada", "Habilidade estratégica"], "Força aumentada", ["Fadiga", "Vulnerabilidade a venenos"], 3000)

def main():
    interface = Interface()
    inicializar_vingadores()

    while True:
        interface.exibir_menu()
        opcao = interface.obter_entrada("Escolha uma opção: ")

        if opcao == "1":  # Cadastro de Vingador
            nome_heroi = interface.obter_entrada("Nome do herói: ")
            nome_real = interface.obter_entrada("Nome real: ")
            categoria = interface.obter_entrada("Categoria (Humano, Meta-humano, Androide, Deidade, Alienígena): ")
            poderes = interface.obter_entrada("Poderes (separados por vírgula): ").split(",")
            poder_principal = interface.obter_entrada("Poder principal: ")
            fraquezas = interface.obter_entrada("Fraquezas (separados por vírgula): ").split(",")
            try:
                nivel_forca = int(interface.obter_entrada("Nível de força (0-10000): "))
                Vingador(nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca)
                interface.mostrar_mensagem("Vingador cadastrado com sucesso!")
            except ValueError as e:
                interface.mostrar_mensagem(f"Erro: {e}")

        elif opcao == "2":  # Listar Vingadores
            interface.listar_vingadores()

        elif opcao == "3":  # Convocar Vingador
            nome = interface.obter_entrada("Nome do herói ou nome real: ")
            vingador = Vingador.buscar_vingador(nome)
            if vingador:
                vingador.convocar()
                interface.mostrar_mensagem(f"{vingador.nome_heroi} convocado com sucesso!")
            else:
                interface.mostrar_mensagem("Vingador não encontrado!")

        elif opcao == "4":  # Aplicar Tornozeleira
            nome = interface.obter_entrada("Nome do herói ou nome real: ")
            vingador = Vingador.buscar_vingador(nome)
            if vingador and vingador._convocado:
                vingador.aplicar_tornozeleira()
            else:
                interface.mostrar_mensagem("Erro: Vingador não convocado ou não encontrado!")

        elif opcao == "5":  # Aplicar Chip GPS
            nome = interface.obter_entrada("Nome do herói ou nome real: ")
            vingador = Vingador.buscar_vingador(nome)
            if vingador:
                if vingador._tornozeleira:
                    vingador.aplicar_chip_gps()
                else:
                    interface.mostrar_mensagem("Erro: Tornozeleira precisa ser aplicada primeiro.")
            else:
                interface.mostrar_mensagem("Vingador não encontrado!")

        elif opcao == "6":  # Listar Detalhes de Vingador
            nome = interface.obter_entrada("Nome do herói ou nome real: ")
            vingador = Vingador.buscar_vingador(nome)
            if vingador:
                interface.listar_detalhes(vingador)
            else:
                interface.mostrar_mensagem("Vingador não encontrado!")

        elif opcao == "7":  # Emitir Mandado de Prisão
            nome = interface.obter_entrada("Nome do herói ou nome real: ")
            vingador = Vingador.buscar_vingador(nome)
            if vingador:
                interface.emitir_mandado_prisao(vingador)
            else:
                interface.mostrar_mensagem("Vingador não encontrado!")

        elif opcao == "0":  # Sair
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    main()
