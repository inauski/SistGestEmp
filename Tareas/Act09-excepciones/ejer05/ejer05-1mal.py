class Calculadora(object):

    cont_calculos= 0

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        Calculadora.cont_calculos +=1
        return "Resultado suma:",self.num1 + self.num2

    def restar(self):
        Calculadora.cont_calculos += 1
        return "Resultado resta:", self.num1 - self.num2

    def multiplicar(self):
        try:
            Calculadora.cont_calculos += 1
            return "Resultado multiplicacion:",self.num1 * self.num2
        except ZeroDivisionError:
            raise ZeroDivisionError("Division es cero")

    def dividir(self):
        Calculadora.cont_calculos += 1
        return "Resultado division:", self.num1 / self.num2

    def leer_num(prompt):
        while True:
            try:
                return (float(input( prompt)))

            except ValueError:
                pass

    def leer_signo(promtp):
        while True:
            signo=input(promtp)

            if(signo == "+" or signo == "-" or signo == "*" or signo == "/"):
                return signo



p1 = float(input("Primer operando (0:Terminar): "))
clase = Calculadora
while (p1 != 0.0):
    p2 = float(input("Segundo operando (0:Terminar): "))

    signo = input("signo (+,-,*,/): ")
    if clase.leer_signo(signo):
        if signo == "+":
            print("%.2f" % Calculadora(p1, p2).sumar())
        elif signo == "-":
            print("%.2f" % Calculadora(p1, p2).restar())
        elif signo == "*":
            print("%.2f" % Calculadora(p1, p2).multiplicar())
        elif signo == "/" :
            print("%.2f" % Calculadora(p1, p2).dividir())


print("Total operaciones %d" % Calculadora.cont_calculos)



