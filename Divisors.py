n = int(input("tapez un entier : "))
k = 0
for i in range(1, n+ 1):
    if n%i == 0:
       print(i)
       k = 1
print("Le nombre des diviseurs de ce nombre sont :",k + 1)