import math
class Exercicios:
    def __int__(self): #Construtor
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "Impossível dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self, num1):
        resultado = ""
        for i in range(0,11,1):
            resultado += f'{num1} * {i} = {num1 * i}\n'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        return math.sqrt(num)

    def exercicio01(self):
        msg = ""
        for i in range(1,11,1):
            msg += f'\n{i}'
        return msg

    def exercicio02(self):
        pares = ""
        for i in range(1,21,1):
            if i % 2 == 0:
                pares += f'\n{i}'
        return pares

    def exercicio03(self):
        somar = 0
        for i in range(1,101,1):
            somar += i
        return somar

    def exercicio04(self):
        multiplos = ""
        for i in range(1,51,1):
            if i % 5 == 0:
                multiplos += f'\n{i}'
        return multiplos

    def exercicio05(self, num):
        if num % 2 == 0:
            return "par"
        else:
            return "impar"

    def exercicio06(self, num):
        if num <= 0:
            return "negativo"
        else:
            return "positivo"

    def exercicio07(self,num3):
        resul = ""
        for i in range(0, 11, 1):
            resul += f'{num3} * {i} = {num3 * i}\n'
        return resul




















