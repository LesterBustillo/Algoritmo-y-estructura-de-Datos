from Deque import *

d = Deque(7)


d.insertRight(2)     # Primer elemento 
d.insertRight(5)     # Segundo elemento 
d.insertRight(8)     # Tercer elemento 
d.insertRight(7)     # Cuarto elemneto

# Imprimir el contenido de la cola doble
print('Contenido de la cola doble:', end=' ')
for i in range(d.size):
    print(d.items[(d.front + i) % d.capacity], end=' ')
print()


d.insertLeft(4)


print('Contenido de la cola doble:', end=' ')
for i in range(d.size):
    print(d.items[(d.front + i) % d.capacity], end=' ')
print()


d.removeRight()


print('Contenido de la cola doble:', end=' ')
for i in range(d.size):
    print(d.items[(d.front + i) % d.capacity], end=' ')
print()


d.removeLeft()


print('Contenido de la cola doble:', end=' ')
for i in range(d.size):
    print(d.items[(d.front + i) % d.capacity], end=' ')
print()


d.removeRight()


print('Contenido de la cola doble:', end=' ')
for i in range(d.size):
    print(d.items[(d.front + i) % d.capacity], end=' ')
print()


print('Primer elemento de la cola doble:', d.peekLeft())


print('Último elemento de la cola doble:', d.peekRight())


print('La cola doble está vacía?', d.isEmpty())


print('La cola doble está llena?', d.isFull())