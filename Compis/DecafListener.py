# Generated from Decaf.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete listener for a parse tree produced by DecafParser.
class DecafListener(ParseTreeListener):

    # Enter a parse tree produced by DecafParser#program.
    def enterProgram(self, ctx:DecafParser.ProgramContext):
        pass

    # Exit a parse tree produced by DecafParser#program.
    def exitProgram(self, ctx:DecafParser.ProgramContext):
        pass


    # Enter a parse tree produced by DecafParser#structDeclara.
    def enterStructDeclara(self, ctx:DecafParser.StructDeclaraContext):
        pass

    # Exit a parse tree produced by DecafParser#structDeclara.
    def exitStructDeclara(self, ctx:DecafParser.StructDeclaraContext):
        pass


    # Enter a parse tree produced by DecafParser#varDecla.
    def enterVarDecla(self, ctx:DecafParser.VarDeclaContext):
        pass

    # Exit a parse tree produced by DecafParser#varDecla.
    def exitVarDecla(self, ctx:DecafParser.VarDeclaContext):
        pass


    # Enter a parse tree produced by DecafParser#methodDecla.
    def enterMethodDecla(self, ctx:DecafParser.MethodDeclaContext):
        pass

    # Exit a parse tree produced by DecafParser#methodDecla.
    def exitMethodDecla(self, ctx:DecafParser.MethodDeclaContext):
        pass


    # Enter a parse tree produced by DecafParser#normal.
    def enterNormal(self, ctx:DecafParser.NormalContext):
        pass

    # Exit a parse tree produced by DecafParser#normal.
    def exitNormal(self, ctx:DecafParser.NormalContext):
        pass


    # Enter a parse tree produced by DecafParser#lista.
    def enterLista(self, ctx:DecafParser.ListaContext):
        pass

    # Exit a parse tree produced by DecafParser#lista.
    def exitLista(self, ctx:DecafParser.ListaContext):
        pass


    # Enter a parse tree produced by DecafParser#structDeclaration.
    def enterStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#structDeclaration.
    def exitStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#varType.
    def enterVarType(self, ctx:DecafParser.VarTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#varType.
    def exitVarType(self, ctx:DecafParser.VarTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#metoInt.
    def enterMetoInt(self, ctx:DecafParser.MetoIntContext):
        pass

    # Exit a parse tree produced by DecafParser#metoInt.
    def exitMetoInt(self, ctx:DecafParser.MetoIntContext):
        pass


    # Enter a parse tree produced by DecafParser#metoChar.
    def enterMetoChar(self, ctx:DecafParser.MetoCharContext):
        pass

    # Exit a parse tree produced by DecafParser#metoChar.
    def exitMetoChar(self, ctx:DecafParser.MetoCharContext):
        pass


    # Enter a parse tree produced by DecafParser#metoBool.
    def enterMetoBool(self, ctx:DecafParser.MetoBoolContext):
        pass

    # Exit a parse tree produced by DecafParser#metoBool.
    def exitMetoBool(self, ctx:DecafParser.MetoBoolContext):
        pass


    # Enter a parse tree produced by DecafParser#metoVoid.
    def enterMetoVoid(self, ctx:DecafParser.MetoVoidContext):
        pass

    # Exit a parse tree produced by DecafParser#metoVoid.
    def exitMetoVoid(self, ctx:DecafParser.MetoVoidContext):
        pass


    # Enter a parse tree produced by DecafParser#single_parameterDeclaration.
    def enterSingle_parameterDeclaration(self, ctx:DecafParser.Single_parameterDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#single_parameterDeclaration.
    def exitSingle_parameterDeclaration(self, ctx:DecafParser.Single_parameterDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#int_parameterType.
    def enterInt_parameterType(self, ctx:DecafParser.Int_parameterTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#int_parameterType.
    def exitInt_parameterType(self, ctx:DecafParser.Int_parameterTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#char_parameterType.
    def enterChar_parameterType(self, ctx:DecafParser.Char_parameterTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#char_parameterType.
    def exitChar_parameterType(self, ctx:DecafParser.Char_parameterTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#boolean_parameterType.
    def enterBoolean_parameterType(self, ctx:DecafParser.Boolean_parameterTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#boolean_parameterType.
    def exitBoolean_parameterType(self, ctx:DecafParser.Boolean_parameterTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#block.
    def enterBlock(self, ctx:DecafParser.BlockContext):
        pass

    # Exit a parse tree produced by DecafParser#block.
    def exitBlock(self, ctx:DecafParser.BlockContext):
        pass


    # Enter a parse tree produced by DecafParser#statement.
    def enterStatement(self, ctx:DecafParser.StatementContext):
        pass

    # Exit a parse tree produced by DecafParser#statement.
    def exitStatement(self, ctx:DecafParser.StatementContext):
        pass


    # Enter a parse tree produced by DecafParser#ifStmt.
    def enterIfStmt(self, ctx:DecafParser.IfStmtContext):
        pass

    # Exit a parse tree produced by DecafParser#ifStmt.
    def exitIfStmt(self, ctx:DecafParser.IfStmtContext):
        pass


    # Enter a parse tree produced by DecafParser#whileStmt.
    def enterWhileStmt(self, ctx:DecafParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by DecafParser#whileStmt.
    def exitWhileStmt(self, ctx:DecafParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by DecafParser#returnStmt.
    def enterReturnStmt(self, ctx:DecafParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by DecafParser#returnStmt.
    def exitReturnStmt(self, ctx:DecafParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by DecafParser#location.
    def enterLocation(self, ctx:DecafParser.LocationContext):
        pass

    # Exit a parse tree produced by DecafParser#location.
    def exitLocation(self, ctx:DecafParser.LocationContext):
        pass


    # Enter a parse tree produced by DecafParser#cond_op_expr.
    def enterCond_op_expr(self, ctx:DecafParser.Cond_op_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#cond_op_expr.
    def exitCond_op_expr(self, ctx:DecafParser.Cond_op_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#boolliteral_expr.
    def enterBoolliteral_expr(self, ctx:DecafParser.Boolliteral_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#boolliteral_expr.
    def exitBoolliteral_expr(self, ctx:DecafParser.Boolliteral_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#loca_expr.
    def enterLoca_expr(self, ctx:DecafParser.Loca_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#loca_expr.
    def exitLoca_expr(self, ctx:DecafParser.Loca_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#num_expr.
    def enterNum_expr(self, ctx:DecafParser.Num_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#num_expr.
    def exitNum_expr(self, ctx:DecafParser.Num_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_op_expr.
    def enterArith_op_expr(self, ctx:DecafParser.Arith_op_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_op_expr.
    def exitArith_op_expr(self, ctx:DecafParser.Arith_op_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#parentesisexpr_expr.
    def enterParentesisexpr_expr(self, ctx:DecafParser.Parentesisexpr_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#parentesisexpr_expr.
    def exitParentesisexpr_expr(self, ctx:DecafParser.Parentesisexpr_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#rel_op_expr.
    def enterRel_op_expr(self, ctx:DecafParser.Rel_op_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#rel_op_expr.
    def exitRel_op_expr(self, ctx:DecafParser.Rel_op_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#methodCall_expr.
    def enterMethodCall_expr(self, ctx:DecafParser.MethodCall_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#methodCall_expr.
    def exitMethodCall_expr(self, ctx:DecafParser.MethodCall_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#charliteral_expr.
    def enterCharliteral_expr(self, ctx:DecafParser.Charliteral_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#charliteral_expr.
    def exitCharliteral_expr(self, ctx:DecafParser.Charliteral_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_higher_expr.
    def enterArith_higher_expr(self, ctx:DecafParser.Arith_higher_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_higher_expr.
    def exitArith_higher_expr(self, ctx:DecafParser.Arith_higher_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#negativo_expr.
    def enterNegativo_expr(self, ctx:DecafParser.Negativo_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#negativo_expr.
    def exitNegativo_expr(self, ctx:DecafParser.Negativo_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#eq_op_expr.
    def enterEq_op_expr(self, ctx:DecafParser.Eq_op_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#eq_op_expr.
    def exitEq_op_expr(self, ctx:DecafParser.Eq_op_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#negacion_expr.
    def enterNegacion_expr(self, ctx:DecafParser.Negacion_exprContext):
        pass

    # Exit a parse tree produced by DecafParser#negacion_expr.
    def exitNegacion_expr(self, ctx:DecafParser.Negacion_exprContext):
        pass


    # Enter a parse tree produced by DecafParser#methodCall.
    def enterMethodCall(self, ctx:DecafParser.MethodCallContext):
        pass

    # Exit a parse tree produced by DecafParser#methodCall.
    def exitMethodCall(self, ctx:DecafParser.MethodCallContext):
        pass


    # Enter a parse tree produced by DecafParser#arg.
    def enterArg(self, ctx:DecafParser.ArgContext):
        pass

    # Exit a parse tree produced by DecafParser#arg.
    def exitArg(self, ctx:DecafParser.ArgContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_higher_op.
    def enterArith_higher_op(self, ctx:DecafParser.Arith_higher_opContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_higher_op.
    def exitArith_higher_op(self, ctx:DecafParser.Arith_higher_opContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_op.
    def enterArith_op(self, ctx:DecafParser.Arith_opContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_op.
    def exitArith_op(self, ctx:DecafParser.Arith_opContext):
        pass


    # Enter a parse tree produced by DecafParser#rel_op.
    def enterRel_op(self, ctx:DecafParser.Rel_opContext):
        pass

    # Exit a parse tree produced by DecafParser#rel_op.
    def exitRel_op(self, ctx:DecafParser.Rel_opContext):
        pass


    # Enter a parse tree produced by DecafParser#eq_op.
    def enterEq_op(self, ctx:DecafParser.Eq_opContext):
        pass

    # Exit a parse tree produced by DecafParser#eq_op.
    def exitEq_op(self, ctx:DecafParser.Eq_opContext):
        pass


    # Enter a parse tree produced by DecafParser#cond_op.
    def enterCond_op(self, ctx:DecafParser.Cond_opContext):
        pass

    # Exit a parse tree produced by DecafParser#cond_op.
    def exitCond_op(self, ctx:DecafParser.Cond_opContext):
        pass


    # Enter a parse tree produced by DecafParser#bool_literal.
    def enterBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#bool_literal.
    def exitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass


