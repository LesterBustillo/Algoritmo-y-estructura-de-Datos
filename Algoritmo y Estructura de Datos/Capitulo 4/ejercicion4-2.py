# Ejercicio 4.2
# Cree un programa que determine si una cadena de entrada es un palíndromo.
# Ejemplos de Palindomos Oso,reconocer,Arriba la birra, Atar a la rata.

stack=[] # Crea una pila para guardar letras

frase=input("Frase a invertir:")#lee la frase
frase = frase.lower() #convierte frase en minuscula
frase = frase.replace(" ","") #Quita espacios en vacios

for i in range(0,len(frase)):
    stack.append(frase[i])
    
inversa = "" 
while(stack) :
   inversa += stack.pop() #Ordena la frase horizontalmente
print("El Invers es", inversa )  

if frase == inversa:
    print("La Frase:",frase ,"es un POLINDROMO")
else:
    print("La frase :",frase,"No es un POLINRDROMO")    



