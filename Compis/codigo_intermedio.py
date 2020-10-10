from DecafParser import DecafParser
from DecafVisitor import DecafVisitor
from tablas_simbolos import *

class codigo_intermedio(DecafVisitor):
    def __init__(self, tipos, metodos, simbolos):
        self.tipos = tipos
        self.metodos = metodos
        self.simbolos = simbolos
        self.temp= []
        self.expr_art = []
        self.expr_high = []
        self.operacion = []
        self.quien = []
    
    def visitStatement(self, ctx:DecafParser.StatementContext):
        print("SDA")
        if len(self.expr_art or self.expr_high) >0:
            print(self.expr_art)
            print(self.expr_high)
            print(self.operacion)
            print(self.quien)
            self.quien = []
            self.operacion = []
            self.expr_art = []
            self.expr_high = []
            self.multi = []
            
        try:
            self.quien.append(ctx.location().getText())
        except:
            pass
        print("ASDFASDFKJASDKJFASKJDFHJASDF")
        print(ctx)

        print(ctx.getText())
        return self.visitChildren(ctx)   
    # Visit a parse tree produced by DecafParser#expression.
############################################################################################

    # Visit a parse tree produced by DecafParser#location.
    def visitLocation(self, ctx:DecafParser.LocationContext):

        print(ctx.getText())
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by DecafParser#statement.

    
    # Visit a parse tree produced by DecafParser#program.
    def visitProgram(self, ctx:DecafParser.ProgramContext):
        print("AS")
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by DecafParser#location.
    def visitLocation(self, ctx:DecafParser.LocationContext):

        print("LOCATION")
        print(ctx.getText())
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cond_op_expr.
    def visitCond_op_expr(self, ctx:DecafParser.Cond_op_exprContext):
        print("CONOP")
        print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#boolliteral_expr.
    def visitBoolliteral_expr(self, ctx:DecafParser.Boolliteral_exprContext):
        print("BOOLEXP")
        print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#loca_expr.
    def visitLoca_expr(self, ctx:DecafParser.Loca_exprContext):

        print("LOCAEXP")
        print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arith_op_expr.
    def visitArith_op_expr(self, ctx:DecafParser.Arith_op_exprContext):
        print(ctx.getText())
        print("ARITHOP")
        print("IZQUIERDA")
        print(ctx.izquierda.getText())
        print("DERECHA")
        print(ctx.derecha.getText())
        print("s")
        self.expr_art.append([ctx.derecha.getText(),ctx.arith_op().getText() ,ctx.izquierda.getText()])

        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#parentesisexpr_expr.
    def visitParentesisexpr_expr(self, ctx:DecafParser.Parentesisexpr_exprContext):
        print("PARENTESIS")
        print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#rel_op_expr.
    def visitRel_op_expr(self, ctx:DecafParser.Rel_op_exprContext):
        print("RELOP")
        print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#methodCall_expr.
    def visitMethodCall_expr(self, ctx:DecafParser.MethodCall_exprContext):
        print("METTHODCALL")
        print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#charliteral_expr.
    def visitCharliteral_expr(self, ctx:DecafParser.Charliteral_exprContext):
        print("CHARLITERA")
        print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arith_higher_expr.
    def visitArith_higher_expr(self, ctx:DecafParser.Arith_higher_exprContext):
        print("IZQUIERDA")
        print(ctx.izquierda.getText())
        print("DERECHA")
        print(ctx.derecha.getText())
        print("HIGHEREXPR")
        print(ctx.getText())
        print(ctx.getText())
        self.operacion.append(ctx.getText())
        self.expr_high.append([ctx.derecha.getText(),ctx.arith_higher_op().getText() ,ctx.izquierda.getText()])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#negativo_expr.
    def visitNegativo_expr(self, ctx:DecafParser.Negativo_exprContext):
        print("NEGATIVO")
        print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#eq_op_expr.
    def visitEq_op_expr(self, ctx:DecafParser.Eq_op_exprContext):
        print("EQOPEXPR")
        print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#negacion_expr.
    def visitNegacion_expr(self, ctx:DecafParser.Negacion_exprContext):
        print("NEGACION")
        print(ctx.getText())
        return self.visitChildren(ctx)


##################3######################################################################
    
       # Visit a parse tree produced by DecafParser#ifStmt.
    def visitIfStmt(self, ctx:DecafParser.IfStmtContext):
        print("EA")
        print(ctx.getText())
        print("s")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafParser#whileStmt.
    def visitWhileStmt(self, ctx:DecafParser.WhileStmtContext):
        return self.visitChildren(ctx)