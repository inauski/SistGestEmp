def esvalido():
    if len(contras) < 8:
        return False
    if contras.__contains__(' '):
        return False
    if contras.isalnum():
        return False
    if contras.islower():
        return False
    if contras.isupper():
        return False
    for i in num:
        if contras.__contains__(str(i)):
            return True
    return False

num = [1,2,3,4,5,6,7,8,9,0]
contras = input("Escribe una contraseña: ")
if esvalido():
    print ("Contraseña valida")
else:
    print ("La contraseña elegida no es segura")
