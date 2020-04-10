class Endereco():
    def __init__(self, rua, numero, complemento, bairro, cidade, pais):
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__pais = pais

    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def pais(self):
        return self.__pais
class Cliente():
    def __init__(self, nome, sexo, data_nascimento, email, profissao, endereco):
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nascimento = data_nascimento
        self.__email = email
        self.__profissao = profissao
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    ''' somente esse com erro:
    @pais.setter
    def pais(self, pais):
        self.__pais = pais'''