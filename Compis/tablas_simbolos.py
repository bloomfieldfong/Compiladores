class simbolos:
    def __init__(self, nombre, tipo, ambito, tamano, offset):
        self.nombre = nombre
        self.tipo = tipo
        self.ambito = ambito
        self.tamano = tamano
        self.offset = offset     
    
    def comparacion_simb(simb2, simb):
        x = 0
        for i in range(len(simb2)):
            if (simb2[i].nombre == simb.nombre and simb2[i].tipo == simb.tipo and simb2[i].ambito == simb.ambito and simb2[i].tamano == simb.tamano):
                x +=1
        if x == 0:
            return True
        else:
            return False
    
    def print_simbolo(self):
        return [self.nombre,self.tipo,self.ambito,self.tamano,self.offset]
    
    def num_or_no(simb, palabra):
        for i in range(len(simb)):
            if simb[i].nombre == palabra:
                return True
        
        return False
    
    def get_type(nombre, tabla):
        respuesta = []
        for i in range(len(tabla)):
            if tabla[i].nombre == nombre:
                respuesta.append([tabla[i].tipo, nombre, tabla[i].ambito])
        return respuesta
        
    def prints(hola):
        for i in range(len(hola)):
            print(hola[i].nombre,hola[i].tipo,hola[i].ambito,hola[i].tamano,hola[i].offset)

class tipos:
    def __init__(self, nombre, tipo, tamano, ambito, offset):
        self.nombre = nombre
        self.tipo = tipo
        self.ambito = ambito
        self.tamano = tamano
        self.offset = offset
        
    def comparacion_tipos(simb2, simb):
        x = 0
        for i in range(len(simb2)):
            if (simb2[i].nombre == simb.nombre and simb2[i].tipo == simb.tipo and simb2[i].ambito == simb.ambito and simb2[i].tamano == simb.tamano):
                x +=1
        if x == 0:
            return True
        else:
            return False
        
    
    def print_tipo(amix):
        print([amix.nombre, amix.tipo, amix.ambito,amix.tamano,amix.offset])

        
class metodos:
    def __init__(self, nombre, tipo, ambito, param):
        self.nombre = nombre
        self.tipo = tipo
        self.ambito = ambito
        self.param  = param
        
    def comparacion_metodo(simb2, simb):
        x = 0
        for i in range(len(simb2)):
            if (simb2[i].nombre == simb.nombre and simb2[i].tipo == simb.tipo and simb2[i].ambito == simb.ambito and simb2[i].param == simb.param):
                x += 1
        if x == 0:
            return True
        else:
            return False
        
    def print_metodo(self):
        return [self.nombre,self.tipo,self.ambito,str(self.param)]

    
    def mismo_return(tipo, retorno, tabla):
        print("")
        

        
    def misma_cant(metodo, tabla, ints):
        
        nombre = metodo[1][1]
        parametros = []
        
        for i in range(len(metodo)):
            if metodo[i][1] == "location":
                parametros.append(simbolos.get_type(metodo[i+1][1], ints))

        f = []
        
        for e in range(len(parametros)):
            s = parametros[e]
            for x in range(len(s)):
                f.append(s[x][0])
            
            
        for i in range(len(tabla)):
            if nombre == tabla[i].nombre and f == tabla[i].param:
                return True
            else:
                return False
    
        
        
        

    

