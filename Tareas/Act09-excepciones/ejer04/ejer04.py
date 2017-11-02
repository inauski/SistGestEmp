class Factorial:
    def __init__(self,numero):
        self.numero = numero

    def factor(self):
        fact = 1
        for i in range(1,self.numero):
            fact = fact + (fact*i)
        return fact

while True:
    try:
        num = int(input("Introduce entero mayor que 0: "))
        #if num >=0 raise
        assert (num >= 0),"Numero tiene que ser >=0"
        f = Factorial(num)
        print("Factorial de", num ,":", f.factor())
        break
    except ValueError:
        print("Error, introduce entero")
    except AssertionError as err:
        print(err)


