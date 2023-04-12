from SimpleStack import *

stack = Stack(50) 
pala = input("Escribe la palabra a invertir: ")

for let in pala: 
    if not stack.isFull(): 
        stack.push(let)

reverb = '' 

while not stack.isEmpty(): 
    reverb += stack.pop()

print('El inverso de ', pala, 'es', reverb)


clean_word = ''.join(e.lower() for e in pala if e.isalpha())

for let in clean_word: 
    if not stack.isFull(): 
        stack.push(let)

reverb = '' 

while not stack.isEmpty(): 
    reverb += stack.pop()

if clean_word == reverb:
    print(pala, 'es un palíndromo.')
else:
    print(pala, 'no es un palíndromo.')
