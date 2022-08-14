conjuntos = []

with open('teste.txt') as teste:
    for line in teste:
        conjuntos.append(line.strip().replace(" ","").split(","))

operacoes = int(conjuntos[0][0])
count = 0
num = int((operacoes*3)-1/2)


def uniao(lista1,lista2):
    lista_final = list(set(lista1 + lista2))
    return lista_final

def inter(lista1,lista2):
    
    lista_final = []
    
    for i in lista1:
        if i in lista2:
            lista_final.append(i)
    
    return lista_final

def dif(lista1, lista2):
    
    lista_final = []
    
    for i in lista1:
        if i not in lista2:
            lista_final.append(i)
            
    return lista_final

def cartesiano(lista1, lista2):
    
    lista_final = []
    
    for i in lista1:
        for c in lista2:
            lista_final.append((i,c))
    return lista_final

def print_resultado(lista1, lista2, lista_final, op):
    check = False


    if type(lista_final[0])== tuple:
        check = True


    lista1 = ",".join(lista1)
    lista2 = ",".join(lista2)
    if check == True:
        lista_final = str(lista_final)

        lista_final = lista_final.replace("[","")

        lista_final = lista_final.replace("]","")
    else:
        lista_final = ",".join(lista_final)


    print(f"{op}: conjunto 1 {{{lista1}}}, conjunto 2 {{{lista2}}}. Resultado: {{{lista_final}}}")
            

for i in range(1, num, 3):
        if conjuntos[i][0]=='U':
            conjunto_uniao = uniao(conjuntos[i+1], conjuntos[i+2])
            print_resultado(conjuntos[i+1], conjuntos[i+2], conjunto_uniao, "União")
        elif conjuntos[i][0]=='I':
            conjunto_inter = inter(conjuntos[i+1], conjuntos[i+2])
            print_resultado(conjuntos[i+1], conjuntos[i+2], conjunto_inter, "Intersecção")
        elif conjuntos[i][0]=='D':
            conjunto_dif = dif(conjuntos[i+1], conjuntos[i+2])
            print_resultado(conjuntos[i+1], conjuntos[i+2], conjunto_dif, "Diferença")
        elif conjuntos[i][0]=='C':
            conjunto_cartesiano = cartesiano(conjuntos[i+1], conjuntos[i+2])
            print_resultado(conjuntos[i+1], conjuntos[i+2], conjunto_cartesiano, "Produto Cartesiano")
        else:
            print("ERRO NO TXT")

