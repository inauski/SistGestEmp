def leer(op):
    op = op.upper()
    assert op in ("A", "B", "M"), "Opción no es A-B-M"
    return op


while True:
    try:
        op = input("Ingresa A (Altas) - B (Bajas) - M (Modificaciones): ")
        print(leer(op))
        break
    except AssertionError as err:
        print(err)


# op=""
# op = op.upper()
# assert op in (("A","B","M"), "Opcion no es A-B-M")
# while True:
#
#
#     try:
#         op = input("Ingresa A (Altas) - B (Bajas) - M (Modificaciones): ")
#
#         if op == "A" or 'a':
#             print("Ha tecleado A")
#             break
#         elif op == "B" or 'b':
#             print("Ha tecleado B")
#             break
#         elif op == "M" or 'm':
#             print("Ha tecleado M")
#             break
#
#     except AssertionError as err:
#             print(err)
