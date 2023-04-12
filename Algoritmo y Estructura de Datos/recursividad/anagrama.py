def anagrama(palabra):
 if len(palabra)<=1:
   return[palabra]
 result=[]
 for part in anagrama( palabra [1:]):
  for i in range(len(part)+1):
     result.append(
       part[:i]+
       palabra [0]+
       part[i:] )
 return result     