"""
Listas

Una lista es una estructura de datos que contiene una secuencia de elementos
de cierto tipo, las listas no son arreglos, ya que las listas no tienen un 
tamaño fijo, un arreglo si; esta característica las hace flexibles y muy 
atractivas de usar para diferentes soluciones de desarrollo.

Para mantener esta flexibilidad de crecimiento es necesario implementar una
lista enlazada, la cual permite crear objetos en memoria no secuencial 
y recalco "EN MEMORIA", de forma lógica si lo deben ser.

Lista enlazada

Una lista enlazada es una colección de objetos llamados nodos, en el cual cada
uno de ellos contiene un campo interno que apunta al siguiente elemento, lo
cual permitirá un recorrido transversal sobre la estructura. La imagen de una
lista ligada simple es la siguiente:
    
    inserte imagen aqui
    
    head                                tail
    
Existe un elemento head (cabeza) que indica el punto de entrada a la estructura,
el elemento final de la misma es conocida como tail (cola).

"""

class Nodo:
    
    def __init__(self,value,siguiente=None):
        self.data = value
        self.next = siguiente
        
#ADT Linked list
        
class Linked_list:
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def get_tail(self):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        return cur_node
    
    def append(self, value):
        if self.is_empty():
            self.head = Nodo(value)
        else:
            self.get_tail().next = Nodo(value)
        
    def transversal(self):
        cur_node = self.head
        if self.head == None:
            print("No hay nodos")
        else:
            while cur_node.next != None:
                print(cur_node.data,"-> ",end='')
                cur_node = cur_node.next
            print(cur_node.data)
        
    def prepend(self,value):
        self.head = Nodo(value,self.head)

# Tarea
        
    def add_before(self,ref_value,value):
        cur_node = self.head
        if cur_node.data == ref_value:
            self.head = Nodo(value,cur_node)
        else:
            while cur_node.data != ref_value:
                aux = cur_node
                cur_node = cur_node.next
            cur_node = aux
            cur_node.next=Nodo(value,cur_node.next)

    
    def add_after(self,ref_value,value):
        cur_node = self.head
        while cur_node.data != ref_value:
            cur_node = cur_node.next
        cur_node.next=Nodo(value,cur_node.next)
        
    def remove(self,value):
        cur_node = self.head
        if cur_node.data == value:
            self.head = cur_node.next
        else:
            while cur_node.data != value:
                aux = cur_node
                cur_node = cur_node.next
            aux.next = cur_node.next
        
    def pop(self):
        cur_node = self.head
        if cur_node.next == None:
            self.head = None
        else:
            while cur_node.next != None:
                aux = cur_node
                cur_node = cur_node.next
            aux.next = None
            
# Tarea        