palavra1 = input()
palavra2 = input()
palavra3 = input()
if palavra1=="vertebrado":
    if palavra2=="ave":
        if palavra3=="carnivoro":
            print("aguia")
        elif palavra3=="onivoro":
            print("pomba")
    elif palavra2=="mamifero":
        if palavra3=="onivoro":
            print("homem")
        elif palavra3=="herbivoro":
            print("vaca")
if palavra1=="invertebrado":
    if palavra2=="inseto":
        if palavra3=="hematofago":
            print("pulga")
        elif palavra3=="herbivoro":
            print("lagarta")
    elif palavra2=="anelideo":
        if palavra3=="hematofago":
            print("sanguessuga")
        elif palavra3=="onivoro":
            print("minhoca")