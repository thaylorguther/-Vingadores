import os
from vingador import Vingador

class Interface:
    def __init__(self):
        self.titulo = "Sistema de Cadastro dos Vingadores"

    def exibir_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{self.titulo}\n")
        print("1. Cadastro de Vingador")
        print("2. Listar Vingadores")
        print("3. Convocar Vingador")
        print("4. Aplicar Tornozeleira")
        print("5. Aplicar Chip GPS")
        print("6. Listar Detalhes de Vingador")
        print("7. Emitir Mandado de Prisão")
        print("0. Sair")

    def obter_entrada(self, mensagem):
        return input(mensagem)

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
        input("Pressione Enter para continuar...")

    def listar_vingadores(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if not Vingador.lista_vingadores:
            self.mostrar_mensagem("Nenhum vingador cadastrado!")
            return
        print("Vingadores Cadastrados:")
        for vingador in Vingador.lista_vingadores:
            print(f"Herói: {vingador.nome_heroi}, Real: {vingador.nome_real}, Categoria: {vingador.categoria}")

    def listar_detalhes(self, vingador):
        detalhes = vingador.listar_detalhes()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Detalhes de {vingador.nome_heroi}:")
        for chave, valor in detalhes.items():
            print(f"{chave}: {valor}")
        input("Pressione Enter para continuar...")

    def emitir_mandado_prisao(self, vingador):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Mandado de prisão emitido para {vingador.nome_heroi}.")
        input("Pressione Enter para continuar...")

