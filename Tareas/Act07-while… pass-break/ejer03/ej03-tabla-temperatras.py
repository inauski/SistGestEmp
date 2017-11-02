class Grados:
    gc = 0
    gf = 0
    cont_temp = 0
    def __init__(self, centigrados=0, fahrenheit=0):
        Grados.cont_temp += 1
        self.gc = centigrados
        self.gf = fahrenheit
    def aCentigrados(self):
        return ((self.gf - 32)*5/9)
    def aFahrenheit(self):
        return 9/(5*self.gc) + 32
def main():
    maxTemp = 120
    paso = 10
    temp = 10
    while temp <= maxTemp:
        gc = Grados(fahrenheit=temp).aCentigrados()
        print("%d F = %0.3f C" % (temp,gc))
        temp += paso
    print("Total temperaturas convertidas %d" % (Grados.cont_temp))
if __name__ == '__main__':
    main()

