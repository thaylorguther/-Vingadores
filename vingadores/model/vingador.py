class Vingador:
    lista_vingadores = []

    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca):
        if categoria not in ['Humano', 'Meta-humano', 'Androide', 'Deidade', 'Alienígena']:
            raise ValueError("Categoria inválida.")
        
        if not (0 <= nivel_forca <= 10000):
            raise ValueError("Nível de força deve ser entre 0 e 10000.")

        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_forca = nivel_forca
        self._convocado = False
        self._tornozeleira = False
        self._chip_gps = False

        Vingador.lista_vingadores.append(self)

    def convocar(self):
        self._convocado = True

    def aplicar_tornozeleira(self):
        if self.nome_heroi == "Thor" or self.nome_heroi == "Hulk":
            print(f"Aviso: {self.nome_heroi} parece estar resistindo à tornozeleira!")
        self._tornozeleira = True

    def aplicar_chip_gps(self):
        if not self._tornozeleira:
            print(f"Erro: Chip GPS não pode ser aplicado sem a tornozeleira!")
            return
        self._chip_gps = True

    def listar_detalhes(self):
        return {
            'Nome do herói': self.nome_heroi,
            'Nome real': self.nome_real,
            'Categoria': self.categoria,
            'Poderes': self.poderes,
            'Poder principal': self.poder_principal,
            'Fraquezas': self.fraquezas,
            'Nível de força': self.nivel_forca,
            'Status de convocação': self._convocado,
            'Status da tornozeleira': self._tornozeleira,
            'Status do chip GPS': self._chip_gps
        }

    @staticmethod
    def buscar_vingador(nome):
        for vingador in Vingador.lista_vingadores:
            if vingador.nome_heroi == nome or vingador.nome_real == nome:
                return vingador
        return None

