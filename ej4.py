terms=int(input("Ingresar número de términos: "))
n,m,j = 0,1,1
count=0
if terms<=0:
    print("Término inválido")
elif terms==1: print(n)
elif terms==2: 
    print(n)
    print(m)
else:
    print("La secuencia de tribonacci es: ")
    while (count<terms):
        print(n)
        sum=n+m+j
        n=m
        m=j
        j=sum
        count=count+1
print("el término n es el último de la sucesión")


    


    
