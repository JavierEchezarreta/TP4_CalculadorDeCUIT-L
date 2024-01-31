def validar_cuit(cuit):
    if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
        return False
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    cuit = cuit.replace("-", "")
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]
    aux = 11 - (aux % 11)
    if aux == 11:
        aux = 0
    if aux == 10:
        aux = 9
    return aux == int(cuit[10])

def tipo_persona (cuit):
    resultado = ""
    tipo = int(cuit[0] + cuit[1])
    genero = ""
    fisica_o_juridica = ""
    if tipo == 20:
        genero = "hombre"
    elif tipo == 27:
        genero = "mujer"
    if tipo == 20 or tipo == 27:
            resultado = f"Persona física ({genero})"
    if tipo == 23 or tipo == 24 or tipo == 25 or tipo == 26:
            resultado = "Persona física (no convencional)"
    if tipo == 30 or tipo == 33 or tipo == 34:
            resultado = "Persona jurídica"
    return resultado

def verificador_correcto (cuit):
        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        cuit = cuit.replace("-", "")
        aux = 0
        for i in range(10):
            aux += int(cuit[i]) * base[i]
        aux = 11 - (aux % 11)
        if aux == 11:
            aux = 0
        if aux == 10:
            aux = 9
        resultado = f"Cuit inválido, su numero verificador es {aux}"
        return resultado

print("::: Bienvenido al verificador de Cuil :::")
while True:
    try: 
        print()
        cuit = input("Ingrese su numero de cuil (incluya los guiones): ")
        if cuit == "0":
            break
        if len(cuit) != 13:
            print()
            print("Número de Cuit inválido, intente nuevamente")
        else:
            if validar_cuit(cuit) is not True:
                print()
                print(verificador_correcto(cuit))
            else:
                print()
                print (tipo_persona(cuit))
    except:
        print("Número de Cuit inválido, intente nuevamente")
