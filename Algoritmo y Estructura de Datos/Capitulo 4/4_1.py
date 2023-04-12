from SimpleStack import *

s = Stack(3)
s.push('A')
s.push('B')
s.push('C')
print(s.items) # ['A', 'B', 'C']

try:
    s.push('D') 
except Exception as e:
    print(e) 
    
s.pop()
s.pop()
s.pop()
print(s.items) # []

try:
    s.pop() 
except Exception as e:
    print(e) 
