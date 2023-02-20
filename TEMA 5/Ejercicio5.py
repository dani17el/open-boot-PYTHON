def añobisiesto():
    año: int = int(input("Introduce un año y veremos si es bisiesto..."))

    if(año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        print(f"¡El año {año} es bisiesto!")
    else:
        print(f"Lo sentimos. El año {año} No es bisiesto!")

print(añobisiesto())