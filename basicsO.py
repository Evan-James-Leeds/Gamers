print(1+2) #O(1)

sum = 0
for i in range(20): #O(n)
    sum+=1
print(str(sum))

sum= 0
for i in range(20): #n O(n^2)
    for j in range(20): #n
        sum+=1
print(str(sum))

