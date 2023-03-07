import random

m = 10
L = []

for i in range(m):
    L.append(random.randint(-10, 10))
    print(L[i], end=' ')

# dodaj instrukcje wyszukiwania
print()

x = int(input("Podaj liczbe:"))
i = 0
for i in L:
 if x in L:
     print("jest")

 else:
     print("nima")

while i < len(L):
    if L[i] == x:
        print("jest liczba:", x)
    i = i+1
if i == len(L):
    print("nie ma ")


