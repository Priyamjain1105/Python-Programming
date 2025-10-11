
l = []
for i in range(20):
     l.append(i)
    
dict = {}
for i in l:
    dict[i]=True;

for i in dict:
    if i == True:
       for j in dict:
           if j%i == 0 and j>i and j>3:
               dict[j] = False

print(dict)
    