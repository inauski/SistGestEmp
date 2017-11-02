produc = {'Bolsas': {'    palomitas':40,
                         'doritos'  :40},
          'Bebidas': {'    fanta'   :40,
                          'cafe'    :40,
                          'aquarius':40}
         }
l = ['palomitas',10,'cafe',40]
def en_despensa(despensa,producto):
    for i in despensa:
        if producto in despensa[i]:
            return i
    return False
def compras(x,l):
    producto = [v for i,v in enumerate(l) if i % 2 == 0]
    cantidad = [v for i,v in enumerate(l) if i % 2 != 0]

    for p,c in list(zip(producto,cantidad)):
        item = en_despensa(x,p)
        if item:
            x[item][p] += c
    return x

print(compras(x, l))

