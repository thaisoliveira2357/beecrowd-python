i = 0
par = 0
impar = 0
positivo = 0
negativo = 0
while i<5:
    num = int(input())
    if num%2==0:
        par += 1
    else:
        impar += 1
    if num>0:
        positivo +=1
    elif num<0:
        negativo +=1
    i +=1
print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")