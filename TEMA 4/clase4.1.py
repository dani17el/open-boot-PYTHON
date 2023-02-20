
# (a > b) and (c >= b) and (a > c or b >= c)
# (False) and (True) and (False or False)
# False and True and False
# False and False
# False

a = 4
b = 6
c = 7
#   True  and   True
#         True
if a >= 5 and b <= 6:
    print("A es mayor o igual que 5 y B es menor o igual que 6")
elif a >= 6:
    print("A es mayor  o igual que 6")
else:
    print("No se cumple NADA de lo anterior")
print("Fin del IF")