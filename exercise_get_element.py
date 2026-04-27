# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):

    if indice <=len(lista)-1 and indice>=-len(lista)+1:
        return lista[indice]
    else:
        return None
