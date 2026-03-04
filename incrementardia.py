def esAñoBisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def obtenerDiasDelMes(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if esAñoBisiesto(year):
            return 29
        else:
            return 28


# Datos ingresados por el usuario
dia_actual = int(input("Ingrese el día: "))
mes_actual = int(input("Ingrese el mes: "))
año_actual = int(input("Ingrese el año: "))

# Sumar un día
dia_actual += 1

if dia_actual > obtenerDiasDelMes(mes_actual, año_actual):
    dia_actual = 1
    mes_actual += 1
    if mes_actual > 12:
        mes_actual = 1
        año_actual += 1

print("La fecha siguiente es:", dia_actual, "/", mes_actual, "/", año_actual)
