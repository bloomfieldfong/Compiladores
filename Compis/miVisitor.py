from DecafParser import DecafParser
from DecafVisitor import DecafVisitor
from tablas_simbolos import *

class miVisitor(DecafVisitor):
    def __init__(self):
        self.i = 0
        self.simb = []
        self.ambito = "global"
        self.meto = []
        self.tip = []
        self.x = 0
        self.errores = []
        self.tip_i  = 0

    # Visit a parse tree produced by DecafParser#statement.
    def visitStatement(self, ctx:DecafParser.StatementContext):
        
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#ifStmt.
    def visitIfStmt(self, ctx:DecafParser.IfStmtContext):


        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#whileStmt.
    def visitWhileStmt(self, ctx:DecafParser.WhileStmtContext):
        return self.visitChildren(ctx)


################################################################ SIMBOLOS #######################################################
    #Simbolos
    #[nombre, tipo, ambito, tamano, offset]
    #nombre =str(ctx.Id())
    #tipo = str(ctx.vartype.getText())
    #ambito = self.ambito
    #tamaño = "4"
    #offset = str(self.i)
    # VISITA VAIRABLE NORMAL

    # Visit a parse tree produced by DecafParser#struct.
    def visitNormal(self, ctx:DecafParser.NormalContext):
        print(self.errores)
        print("33333333333333333333333333333333333333333333333")
        simbolos.prints(self.simb)   
        if self.x == 0:
            self.ambito = "global"
        else:
            self.x = self.x - 1
            
        if self.ambito == "global":
            ## si la variable es y es int
            x = ctx.vartype.getText()
            print(ctx.vartype.getText())
            h = x.split("struct")
            if len(h) > 1:
                #[nombre, tipo, ambito, tamano, offset]
                
                x = simbolos(str(ctx.Id()), ctx.vartype.Id(), self.ambito, "4", str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i += 4
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+str(ctx.Id())+" ya existe")   
                print("--------------------------------------------------")
            if ctx.vartype.getText() == "int":
                x = simbolos(str(ctx.Id()),str(ctx.vartype.getText()),self.ambito,"4",str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i += 4
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+str(ctx.Id())+" ya existe")                   
            ## si la variable es y es char o boolean   
            if ctx.vartype.getText() == "char" or ctx.vartype.getText() == "boolean":
                x = simbolos(str(ctx.Id()),str(ctx.vartype.getText()),self.ambito,"2",str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i +=2
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+str(ctx.Id())+" ya existe")   
        return self.visitChildren(ctx)
    
    # VISITA LISTA
    # Visit a parse tree produced by DecafParser#lista.
    def visitLista(self, ctx:DecafParser.ListaContext):
        ##si la variable dentro de b[esta] esta en las variables
        if self.x == 0:
            self.ambito = "global"
        else:
            self.x = self.x - 1
            
        if self.ambito == "global":
            ## num_or_no = busca si la variable dentro de las [] existe
            ## hola[num] busca que num exista en los simbolos
            if simbolos.num_or_no(self.simb, str(ctx.Num())):
                x = simbolos(str(ctx.Id()),str(ctx.vartype.getText()),self.ambito,"0",str(self.i))
                ## si la vairable ya existe
                if simbolos.comparacion_simb(self.simb, x):
                    self.i += 4
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+str(ctx.Id())+" ya existe") 

            else:
                #verifica si es numero
                t = int(ctx.Num().getText()) / 1
                if int(ctx.Num().getText())>=0:
                    if ctx.varType().getText() == "int":
                        x= simbolos(str(ctx.Id()),str(ctx.vartype.getText()),self.ambito,str(4*int(ctx.Num().getText())),str(self.i))
                        self.simb.append(x)
                        self.i +=2  
                    if ctx.varType().getText() == "char" or ctx.vartype.getText() == "boolean":
                        self.simb.append(simbolos(str(ctx.Id()),str(ctx.vartype.getText()),self.ambito,str(2*int(ctx.Num().getText())),str(self.i)))
                        self.i +=2
                        ####Agregar lista a la tabla de simbolos
                        ###[nombre, tipo, ambito, tamano, offset]
                        ## nombre = str(ctx.Id())
                        ## tipo = ctx.vartype.getText()
                        ## tamano = int(ctx.Num().getText()) * 4
                        ## offset = self.offset
                        ## offset += int(ctx.Num().getText()) * 4       
                else:
                    ##ERROR
                    self.errores.append("Numero negativo")  

        return self.visitChildren(ctx)
    
################################################################ METODOS #######################################################
    # [ nombre, tipo, ambito, param ]
    # nombre = ctx.id()
    # tipo = 
    # parametros =
    # VISITA METODO INT
    def visitMetoInt(self, ctx:DecafParser.MetoIntContext):
        self.ambito = str(ctx.Id())
        ############################
        #Ambito = str(ctx.Id())
        #tipo = int
        #ambito = global
        #parametros = lista_para
        #######PARAMETROS###########
        j = ctx.parameter() 
        lista_para = []
        for i in range(len(j)):
            lista_para.append(j[i].param.getText())
        #############################
        #Simbolos
        #[nombre, tipo, ambito, tamano, offset]
        # agregaremos las variables encontradas aqui #
        # nombre = y[i].Id().getText()
        # tipo = y[i].vartype.getText()
        # ambito =str(ctx.Id())
        # tamaño = 4 
        # offset = self.offset()
        #######BLOCK###########
        block = ctx.block().getText()
        y = ctx.block().varDeclaration()
        for i in range(len(y)):
            self.x = self.x + 1
            nombre = str(y[i].Id().getText())
            tipo = str(y[i].vartype.getText())
            ambito =str(ctx.Id())
            if tipo == "int":
                #[nombre, tipo, ambito, tamano, offset]
                x = simbolos(nombre, tipo, ambito, "4", str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i += 4
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+nombre+" ya existe")                   
            ## si la variable es y es char o boolean   
            if tipo == "char" or nombre == "boolean":
                x = simbolos(nombre,tipo,ambito,"2",str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i +=2
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+nombre+" ya existe")
        
        
        ## ingresar metodos
        me = metodos(str(ctx.Id()), "int","global", str(lista_para))
        print(me)
        if metodos.comparacion_metodo(self.meto,me):
            self.meto.append(me)
        else:
            self.errores.append("La funcion "+str(ctx.Id())+" ya existe")
        return self.visitChildren(ctx)

    # VISITA METODO VOID
    # Visit a parse tree produced by DecafParser#metoVoid.
    def visitMetoVoid(self, ctx:DecafParser.MetoVoidContext):
        print("a----")
        self.ambito = str(ctx.Id())
        ############################
        #Ambito = str(ctx.Id())
        #tipo = int
        #ambito = global
        #parametros = lista_para
        #######PARAMETROS###########
        j = ctx.parameter() 
        lista_para = []
        for i in range(len(j)):
            lista_para.append(j[i].param.getText())
        #############################
        #Simbolos
        #[nombre, tipo, ambito, tamano, offset]
        # agregaremos las variables encontradas aqui #
        # nombre = y[i].Id().getText()
        # tipo = y[i].vartype.getText()
        # ambito =str(ctx.Id())
        # tamaño = 4 
        # offset = self.offset()
        #######BLOCK###########
        block = ctx.block().getText()
        y = ctx.block().varDeclaration()
        print(y)
        print(ctx.Id())
        for i in range(len(y)):
            self.x = self.x + 1
            
            nombre = str(y[i].Id().getText())
            tipo = str(y[i].vartype.getText())
            ambito =str(ctx.Id())
            tamano = "4"

            if tipo == "int":
                x = simbolos(nombre, tipo, self.ambito, "4", str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i += 4
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+nombre+" ya existe")                   
            ## si la variable es y es char o boolean   
            if tipo == "char" or nombre == "boolean":
                print("=----")
                #[nombre, tipo, ambito, tamano, offset]
                x = simbolos(nombre,tipo,self.ambito,"2",str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i +=2
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+nombre+" ya existe")
        
        ## ingresar metodos
        me = metodos(str(ctx.Id()), "int","global", str(lista_para))
        print(me)
        if metodos.comparacion_metodo(self.meto,me):
            self.meto.append(me)
        else:
            self.errores.append("La funcion "+str(ctx.Id())+" ya existe")
            
        ## BLOCK HACER SLIP DE RETURN y si LEN(SPLIT) > 1 THEN ERROR
        f = block.split("return")
        if len(f) >1:
            self.errores.append("El metodo de void tiene return")
        return self.visitChildren(ctx)
   
   # VISITA METODO CHAR
    # Visit a parse tree produced by DecafParser#metoChar.
    def visitMetoChar(self, ctx:DecafParser.MetoCharContext):
        self.ambito = str(ctx.Id())
        ############################
        #Ambito = str(ctx.Id())
        #tipo = int
        #ambito = global
        #parametros = lista_para
        #######PARAMETROS###########
        j = ctx.parameter() 
        lista_para = []
        for i in range(len(j)):
            lista_para.append(j[i].param.getText())
        #############################
        #Simbolos
        #[nombre, tipo, ambito, tamano, offset]
        # agregaremos las variables encontradas aqui #
        # nombre = y[i].Id().getText()
        # tipo = y[i].vartype.getText()
        # ambito =str(ctx.Id())
        # tamaño = 4 
        # offset = self.offset()
        #######BLOCK###########
        block = ctx.block().getText()
        y = ctx.block().varDeclaration()
        for i in range(len(y)):
            self.x = self.x + 1
            
            nombre = str(y[i].Id().getText())
            tipo = str(y[i].vartype.getText())
            ambito =str(ctx.Id())
            
            if tipo == "int":

                x = simbolos(nombre, tipo, ambito, "4", str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i += 4
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+nombre+" ya existe")                   
            ## si la variable es y es char o boolean   
            if tipo == "char" or nombre == "boolean":
                x = simbolos(nombre,tipo,ambito,"2",str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i +=2
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+nombre+" ya existe")
        
        
        ## ingresar metodos
        me = metodos(str(ctx.Id()), "int","global", str(lista_para))
        print(me)
        if metodos.comparacion_metodo(self.meto,me):
            self.meto.append(me)
        else:
            self.errores.append("La funcion "+str(ctx.Id())+" ya existe")
        self.ambito = str(ctx.Id())
        return self.visitChildren(ctx)
 
    # VISITA METODO BOOL
    # Visit a parse tree produced by DecafParser#metoBool.
    def visitMetoBool(self, ctx:DecafParser.MetoBoolContext):
        self.ambito = str(ctx.Id())
        ############################
        #Ambito = str(ctx.Id())
        #tipo = int
        #ambito = global
        #parametros = lista_para
        #######PARAMETROS###########
        j = ctx.parameter() 
        lista_para = []
        for i in range(len(j)):
            lista_para.append(j[i].param.getText())
        #############################
        #Simbolos
        #[nombre, tipo, ambito, tamano, offset]
        # agregaremos las variables encontradas aqui #
        # nombre = y[i].Id().getText()
        # tipo = y[i].vartype.getText()
        # ambito =str(ctx.Id())
        # tamaño = 4 
        # offset = self.offset()
        #######BLOCK###########
        block = ctx.block().getText()
        y = ctx.block().varDeclaration()
        for i in range(len(y)):
            self.x = self.x + 1
            
            nombre = str(y[i].Id().getText())
            tipo = str(y[i].vartype.getText())
            ambito =str(ctx.Id())
            tamano = "4"
            if tipo == "int":
                x = simbolos(nombre, tipo, ambito, tamano, str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i += 4
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+nombre+" ya existe")                   
            ## si la variable es y es char o boolean   
            if tipo == "char" or nombre == "boolean":
                x = simbolos(nombre,tipo,ambito,"2",str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i +=2
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+nombre+" ya existe")
        
        
        ## ingresar metodos
        me = metodos(str(ctx.Id()), "int","global", str(lista_para))
        print(me)
        if metodos.comparacion_metodo(self.meto,me):
            self.meto.append(me)
        else:
            self.errores.append("La funcion ya existe")
        self.ambito = str(ctx.Id())
        return self.visitChildren(ctx)


################################################################ STRUCTS #######################################################
    # Visit a parse tree produced by DecafParser#structDeclaration.
    def visitStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        self.ambito = str(ctx.Id())
        y = ctx.varDeclaration()
        taman = 0
        for i in range(len(y)):
            try:
                num = y[i].Num().getText()
            except:
                num = 1
            self.x += 1
            num = int(num)
            #[nombre, tipo, ambito, tamano, offset]
            if y[i].vartype.getText() == "int":
                x = simbolos(y[i].Id(),y[i].vartype.getText(),self.ambito, str(4*num),str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i +=4*num
                    taman +=4*num
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+y[i].Id(),y[i].vartype.getText()+" ya existe")
            if y[i].vartype.getText() == "boolean" or y[i].vartype.getText() == "char":
                x = simbolos(y[i].Id(),y[i].vartype.getText(),self.ambito, str(2*num),str(self.i))
                if simbolos.comparacion_simb(self.simb, x):
                    self.i +=2*num
                    taman += 2*num
                    self.simb.append(x)
                else:
                    self.errores.append("La variable "+y[i].Id(),y[i].vartype.getText()+" ya existe")
            
            ###[nombre, tipo, tamano, ambito, offset]
            
        x = tipos(str(ctx.Id()), "struct", taman, "global", self.tip_i)
        tipos.print_tipo(x)
        if tipos.comparacion_tipos(self.tip,x):
            self.tip.append(x)
        else:
            self.errores.append("El tipo "+str(ctx.Id())+" ya existe")
            
        for i in range(len(self.tip)):
            tipos.print_tipo(self.tip[i])
            
        return self.visitChildren(ctx)
