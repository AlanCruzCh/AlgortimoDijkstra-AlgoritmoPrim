import networkx as nx
import matplotlib.pyplot as plt

# Definimos los metodos que usaremos para la creacion de nuestro grafo
 
# crear un grafo para la red optimizada
G = nx.Graph() 

# Añade nodos al grafo G
def añadir_nodo(G, nodo):
    G.add_node(nodo)

# Añade las conexiones al grafo
def añadir_conexion(G, nodo_origen, nodo_destino, peso):
    G.add_edge(nodo_origen, nodo_destino, weigth = peso)

# Declaramos una estructura de diccionario la cual nos servira para poder desarrollar el algortimo PRIM 
grafo = {
        # El departamento de Dirección Escolar tiene 4 computadoras en sus sistema, el identificador de este departamento es DE
        # Añadimos las conceciones del equipo numero 1 del departamento DE
        'DE1' : [('DE2',7),('DE3',12), ('DE4',4)],
        # Añadimos las conceciones del equipo numero 2 del departamento DE
        'DE2' : [('DE1',7),('DE3',5)],
        # Añadimos las conceciones del equipo numero 3 del departamento DE
        'DE3' : [('DE2',5),('DE1',12), ('DE4', 10)],
        # Añadimos las conceciones del equipo numero 4 del departamento DE
        'DE4' : [('DE1',4), ('DE3', 10),('SE1',130),('SA2',80),('GE1',66)],

        # El departamento de Subdirección Escolar tiene 2 computadoras en sus sistema, el identificador de este departamento es SA
        # Añadimos las conceciones del equipo numero 1 del departamento SA
        'SA1' : [('SA2',10)],
        # Añadimos las conceciones del equipo numero 1 del departamento SA
        'SA2' : [('SA1',10),('UI1',79),('UP2',100),('DE4', 80)],

        # El departamento de Servicios Estudiantiles tiene 1 computadoras en sus sistema, el identificador de este departamento es SE
        # Añadimos las conceciones del equipo numero 1 del departamento SE
        'SE1' : [('DE4',130),('UP2',55)],
        
        # El departamento de Gestión Escolar tiene 3 computadoras en sus sistema, el identificador de este departamento es GE
        # Añadimos las conceciones del equipo numero 1 del departamento GE
        'GE1' : [('GE2',12),('GE3',4),('UI1',124),('PO2',144),('DE4',66)],
        # Añadimos las conceciones del equipo numero 2 del departamento GE
        'GE2' : [('GE1',12),('GE3',8)],
        # Añadimos las conceciones del equipo numero 1 del departamento GE
        'GE3' : [('GE2',8),('GE1',4)],

        # El departamento de Unidad Informatica tiene 1 computadoras en sus sistema, el identificador de este departamento es UI
        # Añadimos las conceciones del equipo numero 1 del departamento UI
        'UI1' : [('SA2',79),('GE1',124),('DO1',94),('CV1',12)],
        
        # El departamento de UPIS tiene 2 computadoras en sus sistema, el identificador de este departamento es UP
        # Añadimos las conceciones del equipo numero 1 del departamento UP
        'UP1' : [('UP2',3)],
        # Añadimos las conceciones del equipo numero 2 del departamento UP
        'UP2' : [('UP1',3),('SA2',100),('SE1',55)],
        
        # El departamento de Posgrado tiene 5 computadoras en sus sistema, el identificador de este departamento es PO
        # Añadimos las conceciones del equipo numero 1 del departamento PO
        'PO1' : [('PO2',10),('PO3',10), ('PO4',15)],
        # Añadimos las conceciones del equipo numero 2 del departamento PO
        'PO2' : [('PO1',10),('PO3',10),('BI1',37),('DO1',138),('GE1',144)],
        # Añadimos las conceciones del equipo numero 3 del departamento PO
        'PO3' : [('PO2',10),('PO1',10), ('PO5',5)],
        # Añadimos las conceciones del equipo numero 4 del departamento PO
        'PO4' : [('PO1',15),('PO5',20)],
        # Añadimos las conceciones del equipo numero 1 del departamento PO
        'PO5' : [('PO3',5),('PO4',20)],

        # El departamento de Docencía tiene 3 computadoras en sus sistema, el identificador de este departamento es DO
        # Añadimos las conceciones del equipo numero 1 del departamento DO
        'DO1' : [('DO2',7),('DO3',14),('CV1',23),('BI1',105),('UI1',94),('PO2',138)],
        # Añadimos las conceciones del equipo numero 2 del departamento DO
        'DO2' : [('DO1',7),('DO3',14)],
        # Añadimos las conceciones del equipo numero 3 del departamento DO
        'DO3' : [('DO1',7),('DO2',14)],
        
        # El departamento de Campus Virtual tiene 1 computadoras en sus sistema, el identificador de este departamento es CV
        # Añadimos las conceciones del equipo numero 1 del departamento CV
        'CV1' : [('UI1',12),('DO1',23)],
        
        # El departamento de Biblioteca tiene 1 computadora en sus sistema, el identificador de este departamento es BI
        # Añadimos las conceciones del equipo numero 1 del departamento BI
        'BI1' : [('PO2',37),('DO1',105)]
		}

#Añadimos los nodos al grafo
for key in grafo:
    nodo_origen = key
    añadir_nodo(G=G, nodo=nodo_origen)

#Añadimos las conexions con los pesos de cada una de estas
for nodo_origen in grafo:
    for nodo_destino, peso in grafo[nodo_origen]:
        añadir_conexion(G=G, nodo_origen=nodo_origen, nodo_destino=nodo_destino, peso=peso)


# Mostramos el grafo resultante
pos = nx.layout.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, "weigth")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
