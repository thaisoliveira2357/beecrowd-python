idade = int(input())
anos = idade//365
idade = idade - anos*365
meses = idade//30
idade = idade-meses*30
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{idade} dia(s)")