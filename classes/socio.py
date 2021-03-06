class Socio:
    def __init__(self, nome: str, cargo: str, ramal: int):
        self.__nome = nome
        self.__cargo = cargo
        self.__ramal = ramal

# ------------- Acesso aos Atributos -------------

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome : str):
        self.__nome = novo_nome

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, novo_cargo: str):
        self.__cargo = novo_cargo

    def get_ramal(self):
        return self.__ramal

    def set_ramal(self, novo_ramal: int):
        self.__ramal = novo_ramal

    nome = property(get_nome, set_nome)
    cargo = property(get_cargo, set_cargo)
    ramal = property(get_ramal, set_ramal)

# ------------------------------------------------

# ---------------- Magic Methods -----------------

    def __str__(self):
        return f'''------------------------------
         [Sócio Comum]
Nome: {self.__nome}
Cargo: {self.__cargo}
Ramal: {self.__ramal}
------------------------------'''

    def __repr__(self):
        return self.__str__()

# ------------------------------------------------
