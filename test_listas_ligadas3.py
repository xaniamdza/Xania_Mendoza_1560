from listas_enlazadas import *

def main():
    
    lista = Linked_list()
    print(f"Esta vacía?: {lista.is_empty()}")
    lista.append(10)
    lista.append(20)
    lista.append(30)
    lista.append(40)
    lista.append(50)
    lista.transversal()
    print(lista.get_tail().data)
    lista.transversal()
    lista.add_after(10,20)
    lista.transversal()
    lista.add_before(50,89)
    lista.transversal()
    lista.prepend(7)
    lista.transversal()
    lista.remove(89)
    lista.transversal()
    lista.pop()
    lista.transversal()
   
main()