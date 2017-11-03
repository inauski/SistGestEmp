print ("Ejer 5")
usuario = input("Escribe un usuario: ")
valido = True
if not usuario.isalnum():
    print ("El nombre de usuario puede contener solo letras y números")
    valido = False
if len(usuario) < 6:
    print ("El usuario debe tener al menos 6 carácteres")
    valido = False
if len(usuario) > 12:
    print ("El usuario debe tener menos de 12 caracteres")
    valido = False
if valido:
    print ("Usuario validado")
    #valido = True