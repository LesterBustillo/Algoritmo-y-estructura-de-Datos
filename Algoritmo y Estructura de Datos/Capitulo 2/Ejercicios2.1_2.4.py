class Array(object):

 def __init__(self, initialSize): 
    self.__a = [None] * initialSize 
    self.__nItems = 0 
 def __len__(self): 

    return self.__nItems 
 def get(self, n): 

    if 0 <= n and n < self.__nItems: 

        return self.__a[n] 

 def set(self, n, value): 
    if 0 <= n and n < self.__nItems: 

        self.__a[n] = value 

 def insert(self, item): 
    self.__a[self.__nItems] = item 
    self.__nItems += 1 
    
 def find(self, item): 
    for j in range(self.__nItems):
         if self.__a[j] == item: 
            return j 
            return -1 
        
 def search(self, item): 
     return self.get(self.find(item))
 
 def delete(self, item): 
     for j in range(self.__nItems): 
        if self.__a[j] == item: 
         self.__nItems =-1 
         for k in range(j, self.__nItems):
            self.__a[k] = self.__a[k+1] 
        return True 
        return False 
    
 def traverse(self, function=print):
    for j in range(self.__nItems): 
        function(self.__a[j])

#AGREGADO EJERCICIO 2.1
 def getMaxNum(self):
   a=(max(self.__a))
   return a
   
#AGREGADO EJERCICIO 2.2
 def deleteMaxNum(self):
   a=(max(self.__a))
   for j in range(self.__nItems): 
      if self.__a[j] == a: 
       self.__nItems -=1
       #self.__a[a]= self.__a.append(None)
       
       for k in range(j, self.__nItems):
         self.__a[k] = self.__a[k+1] 
      print("Numero max eliminado")           
      return True 
      return False  

#AGREGADO EJERCICIO 2.3
 def deleteOrdenados(self):
   unico=[]
   for i in self.__a:
      if i not in unico :
         unico.append(1)
         unico.sort()
   self.__a=unico
   self.deleteMaxNum()
   print("Ordenados de forma ascendente")     
   
  
#AGREGADO EJERCICIO 2.4
 def removeDups(self):
    unico=[]
    for i in self.__a:
      if i not in unico :
         unico.append(i)
         
    print(unico)