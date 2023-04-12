from OrderedRecordArray import *
def second(x): 
        return x[1]
maxSize = 1000 
arr = OrderedRecordArray(maxSize, second) 

# Insert 10 items
for rec in [('a', 4.2), ('b', 8.0), ('c', 9.0), ('d', 5.4),
 ('e', 6.5), ('f', 3.1), ('g', 0.0), ('h', 6.5),
 ('i', 7.0,) ('j', 6.0),('a', 4.2),('c', 4.0)]:
 arr.insert(rec)
 
print("Array containing", len(arr), "items:\n", arr)


for rec in [('c', 6.0), ('g', 0.0), ('g', 0.0),
 ('b', 7.5), ('i', 7.5)]:
 print("Deleting", rec, "returns", arr.delete(rec))
print("Array after deletions has", len(arr), "items:\n", arr)

for key in [4.4, 6.0, 7.5]:
 print("find(", key, ") returns", arr.find(key),
 "and get(", arr.find(key), ") returns",
arr.get(arr.find(key)))
 
 
arr.merge()
arr.duplicados()
for rec in [('a', 4.2), ('b', 8.0), ('c', 9.0), ('d', 5.4),]:
 arr.maxsize(rec)