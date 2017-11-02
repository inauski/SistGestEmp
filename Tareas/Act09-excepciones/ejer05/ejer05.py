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
        Calculadora.cont_calculos += 1
        return "Resultado multiplicacion:",self.num1 * self.num2

    def dividir(self):
        Calculadora.cont_calculos += 1
        return "Resultado division:", self.num1 / self.num2

    def leer_num(prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                pass #para que siga ejecutando

    def leer_signo(promtp):
        while True:
            try:
                sig = input(promtp)
                assert (sig in ("+","-","*","/")),"Operando incorrecto"
                return sig
            except AssertionError:
                pass

terminar = float(input("Primer operando (0:Terminar): "))
clase = Calculadora
while (terminar != 0.0):
    op = float(input("Segundo operando (0:Terminar): "))
    # while signol == False:
    signo = input("signo (+,-,*,/): ")
    if clase.leer_signo(signo):
        if signo == "+":
            print("%.2f" % Calculadora(terminar, op).sumar())
        elif signo == "-":
            print("%.2f" % Calculadora(terminar, op).restar())
        elif signo == "*":
            print("%.2f" % Calculadora(terminar, op).multiplicar())
        elif signo == "/":
            try:
                print(Calculadora(terminar, op).dividir())
            except ZeroDivisionError:
                print("Divisor es 0")
    z = False
    while z == False:
        try:
            terminar = float(input("Primer operando (0:Terminar): "))
            z = True
        except ValueError:
            z = False
print("Total operaciones %d" % Calculadora.cont_calculos)

# while True:
#
#     n1 = Calculadora.leer_num("Primer operando(0:Terminar): ")
#     if n1 == 0:
#         break
#     signo = Calculadora.leer_signo("Signo(+, -, *, /): ")
#
#     n2 = Calculadora.leer_num("Segundo operando: ")
#     if n2 == 0 and signo == "/":
#         print("Divisor es 0")
#     else:
#         calc = Calculadora(n1,n2)
#         calDicc = {"+":calc.sumar(),"-":calc.restar(),"*":calc.multiplicar(),"/":calc.dividir()}
#         print(calDicc[signo])
# print("Total de operaciones: ", Calculadora.cont_calculos)


