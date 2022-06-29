def list_new():
    list=[]
    for i in range(10):
        valor=input(":: Ingresar un elemento:  ::")
        list.append(valor)  
    return list

def devolver_list(list):
        print(",".join(map(str,list)))       
def ordenar_list(list):
    print(sorted(list))
   
def revertir_list(list):
    list.sort(reverse=True)
    print(list)

def elemento(list):
    if valor in list:
        list.index(valor)
        print(f':: La longitud de la lista es:   :: ',len(list))
        

list=list_new()
print("El contenido de la lista es : ", list)    
rango=devolver_list(list)
ordenar_list(list)
revertir_list(list)
valor=input(":: Ingrese Un Elemento:  ::")
print(list.index(valor))
elemento(list)