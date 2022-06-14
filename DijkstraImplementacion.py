import networkx as nx
import matplotlib.pyplot as plt

'''
    A continuación creamos el grafo en una estructura de datos conocida como diccionario 
    En el podremos saber los distintos nodos que seran los diferentes departamentos que hay en una 
    empresa/escuela
    Y las haristas que conectan a los nodos las cuales tendran una distancia establecida 
    La distancia que se presenta en los vertices es en metros
'''
'''
    A continuacion se enlistara los nombres de los nodos asi como su identidicador 
    Nodo 1: Dirección Escolar Identificador: DE
    Nodo 2: Subdirección Académica Identificador: SA
    Nodo 3: Gestión Escolar Identificador: GE
    Nodo 4: Servcios Estudiantiles Identificador: SE
    Nodo 5: UPIS Identificador: UP
    Nodo 6: Unidad Informatica Identificador: UI
    Nodo 7: Posgrado Identificador: PO
    Nodo 8: Docencia Identificador: DO
    Nodo 9: Campus Virtual Identificador: CV
    Nodo 10: Biblioteca Identificador: BI

'''
grafo = {
            # Nodo 1 Departamento "Direccion"
            'DE': 
            # Se colocan los departamentos con los que tienen conexion el nodo DE 
                [('SA', 80),('SE', 130),('GE', 66)],

            # Nodo 2 Departamento "Subdirección Academica"
            'SA': 
            # Se colocan los departamentos con los que tienen conexion el nodo  SA
                [('DE', 80),('UI', 79),('UP', 100)],

            # Nodo 3 Departamento "Gestión Escolar"
            'GE': 
            # Se colocan los departamentos con los que tienen conexion el nodo direccion 
                [('UI', 124),('PO', 144),('DE', 66)],

            # Nodo 4 Departamento "Servicios Estudiantiles "
            'SE': 
            # Se colocan los departamentos con los que tienen conexion el nodo direccion 
                [('DE', 130),('UP', 55)],

            # Nodo 5 Departamento "UPIS"
            'UP': 
            # Se colocan los departamentos con los que tienen conexion el nodo direccion 
                [('SE', 55),('SA', 100)],

            # Nodo 6 Departamento "Unidad Informatica"
            'UI': 
            # Se colocan los departamentos con los que tienen conexion el nodo direccion 
                [('SA', 79),('GE', 124),('DO', 94),('CV',12)],

            # Nodo 7 Departamento "Posgrado"
            'PO': 
            # Se colocan los departamentos con los que tienen conexion el nodo direccion 
                [('GE', 144),('DO', 138),('BI', 37)],

            # Nodo 8 Departamento "Docencia"
            'DO': 
            # Se colocan los departamentos con los que tienen conexion el nodo direccion 
                [('CV', 23),('UI', 94),('PO', 138),('BI',105)],

            # Nodo 9 Departamento "Campus Virtual"
            'CV': 
            # Se colocan los departamentos con los que tienen conexion el nodo direccion 
                [('UI', 12),('DO', 23)],

            # Nodo 10 Departamento "Direccion "
            'BI': 
            # Se colocan los departamentos con los que tienen conexion el nodo direccion 
                [('PO',37),('DO', 105)]

        }

# Solicitamos al usuario que nos de el nodo origen y  el nodo destino 
origen = input("\nIngresa el nodo origen: ")
destino = input("\nIngrese el nodo destino: ")

# Declaramos arreglos que nos serviran para llevar un mejor control
nodos_visitados = []
recorrido_mas_corto = []
aristas_vecinas_nodo_actual = []

# declaramoa nuestro nodo actual y le agregamos un peso de 0
# el primero es el nodo origen (a)
# el segundo es el peso (b)
# el tercero es nodo destino(c)
nodo_actual = (origen, 0, origen)
posicion_actual = origen

# Vemos que nodos son adyacentes a nuestro nodo origen
for arista_destino, peso_arista in grafo[posicion_actual]:
        peso_aux = nodo_actual[1] + peso_arista
        if peso_aux <= peso_arista:
            aristas_vecinas_nodo_actual.append((posicion_actual, peso_aux, arista_destino))

# Organizamos la lista que obtuvimos con las posiciones adyacentes al nodo origen para asi 
# poder obtener el de menor valor 
aristas_vecinas_nodo_actual = [(b,a,c) for a,b,c in aristas_vecinas_nodo_actual]
aristas_vecinas_nodo_actual.sort()
aristas_vecinas_nodo_actual = [(a,b,c) for b,a,c in aristas_vecinas_nodo_actual]
nodos_visitados.append(origen)

# Declaramos un while que se repetira hasta que alcancemos el nodo al que deseamos llegar 
while posicion_actual != destino:

    # Declaramos una bandera que nos ayudara a controlar la insercion de nuevas haristas 
    bandera = True

    # Tomamos el primer elemento que debe ser la arista con menor valor y lo eliminanos de la lista 
    # de aristas vecinas al nodo acrual
    nodo_actual = aristas_vecinas_nodo_actual.pop(0)
    posicion_actual = nodo_actual[2]
    vertice = nodo_actual[0]

    # Como ya llegamos a ese nodo lo guardamos en la lista que nos ayudara a ver por que posiciones paso 
    # el nodo
    recorrido_mas_corto.append(nodo_actual)

    # Checamos que el nodo al que llegamos esta en la lista de nodos visitados, si no esta lo añadimos ya que 
    # despues nos desplazaremos al nodo siguiente y asi el anterior queda como visitado
    if posicion_actual not in nodos_visitados:
        nodos_visitados.append(posicion_actual)
        
    # Checamos nuevamente las aristas que estan con respecto al nodo actual
    for arista_destino, peso_arista in grafo[posicion_actual]:
            
            # Revisamos que el nodo al que vamos a llegar no este en la lista de nodos visitados por que si lo esta 
            # no podemos desplazarnos hacia el ya que es una condición del algoritmo
            if arista_destino not in nodos_visitados:

                # Calculamos el peso que nos costaria llegar al nodo siguiente
                peso_aux = nodo_actual[1] + peso_arista

                # Comprobamos que si el nodo al que vamos a llegar ya existe en las posibles nodos adyacetes
                for prueaba in aristas_vecinas_nodo_actual:
                    nodo_aux = prueaba
                    if nodo_aux[2] == arista_destino:

                        # Si existe el nodo entonces checamos si el peso para llegar a ese nodo es menor al aux
                        if peso_aux <= nodo_aux[1]: 

                            # Si el peso es menor pasamos a eleminar ese nodo de la lista y rompemos el ciclo
                            posicion_arista = aristas_vecinas_nodo_actual.index(nodo_aux)
                            aristas_vecinas_nodo_actual.pop(posicion_arista)
                            break
                        else:

                            # En el caso de que sea mayor cambiamos el valor de la bandera para que ese nodo que se agrehgara no lo haga
                            bandera = False     

                # Con este comprobamos que mientras la bandera sea verdadera se agregara un nuevo nodo adyacente
                if bandera == True:
                    aristas_vecinas_nodo_actual.append((posicion_actual, peso_aux, arista_destino))
                        
    # Areglamos el carrglo para obtener el de menor peso
    aristas_vecinas_nodo_actual = [(b,a,c) for a,b,c in aristas_vecinas_nodo_actual]
    aristas_vecinas_nodo_actual.sort()
    aristas_vecinas_nodo_actual = [(a,b,c) for b,a,c in aristas_vecinas_nodo_actual]
        
# Declaramos variables que nos ayudaran a obtener el camino mas corto al recorrer la lista que tiene los caminos por los cuales paso el algoritmo
recorrido_fianl =[]
nodo_atras = recorrido_mas_corto[-1]
recorrido_fianl.append(nodo_atras)

# Mientras que el nodo origen que se encuentra en ese arreglo sea diferente al nodo en el que comenzamos el algoritmo 
# repetiremos un while para sacar dicho camino
while nodo_atras[0] != origen:
    
    for nodo_atras_aux in recorrido_mas_corto:
        if nodo_atras_aux[2] == nodo_atras[0]:
            recorrido_fianl.append(nodo_atras_aux)
            nodo_atras = nodo_atras_aux
            break

# Ordenamos la nueva lista que nos muestra el camino mas corto para llegar del nodo origen al destino
recorrido_fianl = [(b,a,c) for a,b,c in recorrido_fianl]
recorrido_fianl.sort()
recorrido_fianl = [(a,b,c) for b,a,c in recorrido_fianl]

# Mostraos el peso final y el camino que se debe seguir
peso_recorrido = recorrido_fianl[-1]
print("\nEl camino mas corto es: ",recorrido_fianl, " y tiene un peso total de: ", peso_recorrido[1], "\n")


# crear un grafo
G = nx.Graph() 

# funcion que nos permitira agregar al nodo al grafo
def añadir_nodo(G, nodo):
    G.add_node(nodo)

# funcion que nos permitira agregar las conexiones a nuestro grafo
def añadir_conexion(G, nodo_origen, nodo_destino, peso):
    G.add_edge(nodo_origen, nodo_destino, weigth = peso)

#Añadimos los nodos al grafo
for key in grafo:
    nodo_origen = key
    añadir_nodo(G=G, nodo=nodo_origen)

#Añadimos las conexions con los pesos de cada una de estas
for nodo_origen in grafo:
    for nodo_destino, peso in grafo[nodo_origen]:
        añadir_conexion(G=G, nodo_origen=nodo_origen, nodo_destino=nodo_destino, peso=peso)

# Desplegamos el grafo 
pos = nx.layout.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, "weigth")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

