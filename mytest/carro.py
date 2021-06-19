'''
    Exercício 1 -  COMPOSIÇÃO


    Enunciado:

        Você deve criar uma classe carro que vai possuir dois atributos
        compostos por outras duas classes:

        1) Motor
        3) Direção

        O motor terá a responsabilidade de controlar a velocidade.
        Ele oferece os seguintes atributos:
        1) Atributo de dado Velocidade
        2) Método Acelerar, o que deverá incrementar a velocidade  de uma unidade
        3) Método Frear, que deverá decrementar a velocidade em duas unidades

        A direção terá a responsabilidade de controlar a direção. Ela oferece os
        seguintes atributos:

        1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
        2) Método girar_a_direita
        3) Método girar_a_esquerda
            N
        O       E
            S

        Exemplo:
        >>> # Testando motor
        >>> motor = Motor()
        >>> motor.velocidade
        0
        >>> motor.acelerar()
        >>> motor.velocidade
        1
        >>> #Testando direção
        >>> direcao = Direcao()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Leste'
        >>> motor = Motor()
        >>> direcao = Direcao()
        >>> carro = Carro(direcao, motor)
        >>> carro.calcular_velocidade()
        0
        >>> carro.calcular_direcao()
        'Norte'
'''
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    rotacao_direita = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_esquerda = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_esquerda[self.valor]


direcao = Direcao()
motor = Motor()

class Carro():

    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()
