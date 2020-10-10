def generar(expr_art, expr_high, operaciones,quien):
#    3*3  +3+3+   3*4*3*3*3
#    exprt_art = [['3*3+3+3', '+', '3*4'], ['3*3+3', '+', '3'], ['3*3', '+', '3']]
#    expr_high = [['3', '*', '3'], ['3', '*', '4']]
#    operaciones = ['3*3', '3*4']
#    quien = ['z.a']
    multi = []
    multi2 = []
    otra = []
    lista = []
    i = 0
    te = 0
    yess = 0
    while i < len(expr_high):
        yes = ["Temp"+str(yess), "Temp"+str(yess+1)]
        temp = expr_high[i]
        if i%2 == 0:
            es = yes[0]
        else:
            es = yes[1]
            
        if i%2 == 0:
            ese = yes[1]
        else:
            ese = yes[0]
        ## si la operacion de la izquierda esta adentro pero la de la derecha no 
        if temp[0] in operaciones and  temp[2] not in operaciones:
            multi2.append(es+"="+ese+" "+temp[1]+" "+temp[2])
            lista.append(operaciones[i])
            
        ## si la operacion de la derecha esta adentro pero la de la izquierda no 
        elif temp[2] in operaciones and temp[0] not in operaciones:
            donde = operaciones.index(temp[2])
            multi2.append(es+"="+temp[0]+" "+temp[1]+" "+ese)
            lista.append(operaciones[i])
            
        ## si ambas estan:
        elif temp[2] in operaciones and temp[0] in operaciones:
            pass
        else:

            lista.append(operaciones[i])
            otra.append(lista)
            lista = []
            multi2.append(es+"="+temp[0]+" "+temp[1]+" "+temp[2])
            multi.append(multi2)
            multi2 = []
            yess +=1
            
        i+=1

    #otra
    #multi
    temporales_usadas = []
    for i in range(len(otra)):
        hola = multi[i][0].split("=")
        otra[i] = [hola[0], otra[i]]
        temporales_usadas.append(hola[0])
    print("OTRA")
    print(otra)
    
#    for i in range(len(multi)):
#        x = multi[i]
#        multi[i] = x[::-1]
#        print(multi[i])
#        
    
    print(multi)
    print(expr_art)
    print("z.a=  3*3   +3+3+     3*4*3*3*3    +     5*1;")
    print("\n")
    final = []
    y = len(temporales_usadas)
    var_nuevas = []
    for i in range(len(expr_art)):
        y+=1

            
        yes = ["Temp"+str(y), "Temp"+str(y+1)]

        temp = expr_art[i]
        izquierdo = []
        derecha = []
        for x in range(len(otra)):
            z = otra[x][1]

            #si el lado izquierdo ya existe
            if temp[0] == z[0]:
                izquierdo.append(otra[x][0])

            #si el lado derecho ya existe
            if temp[2] == z[0]:
                derecha.append(otra[x][0])
                


        if len(derecha)>0:
            final.append(yes[0]+" = "+yes[1]+" "+temp[1]+" "+derecha[0])
            inde = 0
            for er in range(len(otra)):
                po = otra[er]
                if po[0] == derecha[0]:
                    inde = er
            
            for me in range(len(multi[inde])):
                final.append(multi[inde][me])
           
           
        elif len(izquierdo)>0:
            final.append(yes[0]+" = "+izquierdo[0]+" "+temp[1]+" "+temp[2])
            inde = 0
            for er in range(len(otra)):
                po = otra[er]
                if po[0] == izquierdo[0]:
                    inde = er
            
            for me in range(len(multi[inde])):
                final.append(multi[inde][me])
                
            
          
        else:
            final.append(yes[0]+" = "+yes[1]+" "+temp[1]+" "+temp[2])
        
        for i in range(len(derecha)):
            var_nuevas.append(derecha[i])
        for i in range(len(izquierdo)):
            var_nuevas.append(izquierdo[i])
        
        derecha = []
        izquierdo = []
        #print(var_nuevas)
    
    final = final[::-1]
    for i in range(len(final)):
        print(final[i])
    print("\n")
generar([['4*5', '+', '2*3']], [['4', '*', '5'], ['2', '*', '3']], ['4*5', '2*3'], ['z.a'])
generar([['3*3+3+3+3*4*3*3*3', '+', '5*1'], ['3*3+3+3', '+', '3*4*3*3*3'], ['3*3+3', '+', '3'], ['3*3', '+', '3']], [['3', '*', '3'], ['3*4*3*3', '*', '3'], ['3*4*3', '*', '3'], ['3*4', '*', '3'], ['3', '*', '4'], ['5', '*', '1']], ['3*3', '3*4*3*3*3', '3*4*3*3', '3*4*3', '3*4', '5*1'], ['z.a'])
generar([['3*3+3+3+3*4*3', '+', '5*1'], ['3*3+3+3', '+', '3*4*3'], ['3*3+3', '+', '3'], ['3*3', '+', '3']], [['3', '*', '3'], ['3*4', '*', '3'], ['3', '*', '4'], ['5', '*', '1']], ['3*3', '3*4*3', '3*4', '5*1'], ['z.a'])