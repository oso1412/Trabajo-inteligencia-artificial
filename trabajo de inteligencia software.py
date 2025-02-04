
arbol = []
acabo = "no"
numero=int(input("Cual es el numero padre "))
arbol.append(numero)
numerohijos=0

contador=0   




while acabo == "no":
  if arbol[contador]!="":
    
    print("Cuantos hijos tiene el padre ", arbol[contador])
    numerohijos=int(input(""))
    
    if numerohijos==2:
        print("Cual es el numero hijo 1 del padre ", arbol[contador])                                  
        numero=int(input(""))
        arbol.append(numero)
        print("Cual es el numero hijo 2 del padre ", arbol[contador])
        numero=int(input(""))
        arbol.append(numero)
    elif numerohijos==1:
        print("Cual es el numero hijo 1 del padre ", arbol[contador])
        numero=int(input(""))
        arbol.append(numero)
        numero=0
        arbol.append("")
       
    elif numerohijos==0:
        arbol.append("")
        arbol.append("")
       
          
    contador=contador+1

    acabo=input("El arbol acabo?, si o no ")





contador2=0
contador=2
for arbol1 in arbol:

    if contador2==0:
     print(arbol1)

    if contador<contador2:
     contador=contador*2
     contador2=1
     print("")
    contador2=contador2+1
    if contador2!=1:
     print(arbol1, "  " ,end="")
    


