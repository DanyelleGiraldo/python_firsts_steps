x1= str(input("ingrese la palabra 1 "))
x2= str(input("ingrese la palabra 2 "))

lx1= len(x1)
lx2= len(x2)

if lx1 > lx2 :
    print("la palabra", x1 ,"tiene", lx1-lx2, "letras mas que ", x2)
elif lx1<lx2 :
    print("la palabra", x2 ,"tiene", lx2-lx1, "letras mas que ", x1)
else:
    print(x1, "y", x2, "son igual de largas")
