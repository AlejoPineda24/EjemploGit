def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False


def dias_en_mes(mes, anio):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28


# Entrada de datos
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

# Incrementar día
dia += 1

if dia > dias_en_mes(mes, anio):
    dia = 1
    mes += 1
    if mes > 12:
        mes = 1
        anio += 1

print("La fecha del día siguiente es:", dia, "/", mes, "/", anio)