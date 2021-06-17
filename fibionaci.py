

a = 0
b = 1
lengthoflist = []
print('input how many fibionaci numbers you want.')
q= int(input())
for i in range(q):
    c = a + b
    lengthoflist.append(c) 
    a = b
    b = c
print(lengthoflist)
print(lengthoflist[-1] / lengthoflist[-2])

