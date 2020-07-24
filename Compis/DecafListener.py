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


    # Enter a parse tree produced by DecafParser#declaration.
    def enterDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#declaration.
    def exitDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#single_varDeclaration.
    def enterSingle_varDeclaration(self, ctx:DecafParser.Single_varDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#single_varDeclaration.
    def exitSingle_varDeclaration(self, ctx:DecafParser.Single_varDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#array_varDeclaration.
    def enterArray_varDeclaration(self, ctx:DecafParser.Array_varDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#array_varDeclaration.
    def exitArray_varDeclaration(self, ctx:DecafParser.Array_varDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#structDeclaration.
    def enterStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#structDeclaration.
    def exitStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#int_varType.
    def enterInt_varType(self, ctx:DecafParser.Int_varTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#int_varType.
    def exitInt_varType(self, ctx:DecafParser.Int_varTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#char_varType.
    def enterChar_varType(self, ctx:DecafParser.Char_varTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#char_varType.
    def exitChar_varType(self, ctx:DecafParser.Char_varTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#boolean_varType.
    def enterBoolean_varType(self, ctx:DecafParser.Boolean_varTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#boolean_varType.
    def exitBoolean_varType(self, ctx:DecafParser.Boolean_varTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#structImpl_varType.
    def enterStructImpl_varType(self, ctx:DecafParser.StructImpl_varTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#structImpl_varType.
    def exitStructImpl_varType(self, ctx:DecafParser.StructImpl_varTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#structDecl_varType.
    def enterStructDecl_varType(self, ctx:DecafParser.StructDecl_varTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#structDecl_varType.
    def exitStructDecl_varType(self, ctx:DecafParser.StructDecl_varTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#void_varType.
    def enterVoid_varType(self, ctx:DecafParser.Void_varTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#void_varType.
    def exitVoid_varType(self, ctx:DecafParser.Void_varTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#int_methodDeclaration.
    def enterInt_methodDeclaration(self, ctx:DecafParser.Int_methodDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#int_methodDeclaration.
    def exitInt_methodDeclaration(self, ctx:DecafParser.Int_methodDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#char_methodDeclaration.
    def enterChar_methodDeclaration(self, ctx:DecafParser.Char_methodDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#char_methodDeclaration.
    def exitChar_methodDeclaration(self, ctx:DecafParser.Char_methodDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#boolean_methodDeclaration.
    def enterBoolean_methodDeclaration(self, ctx:DecafParser.Boolean_methodDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#boolean_methodDeclaration.
    def exitBoolean_methodDeclaration(self, ctx:DecafParser.Boolean_methodDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#void_methodDeclaration.
    def enterVoid_methodDeclaration(self, ctx:DecafParser.Void_methodDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#void_methodDeclaration.
    def exitVoid_methodDeclaration(self, ctx:DecafParser.Void_methodDeclarationContext):
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


    # Enter a parse tree produced by DecafParser#if_statement.
    def enterIf_statement(self, ctx:DecafParser.If_statementContext):
        pass

    # Exit a parse tree produced by DecafParser#if_statement.
    def exitIf_statement(self, ctx:DecafParser.If_statementContext):
        pass


    # Enter a parse tree produced by DecafParser#while_statement.
    def enterWhile_statement(self, ctx:DecafParser.While_statementContext):
        pass

    # Exit a parse tree produced by DecafParser#while_statement.
    def exitWhile_statement(self, ctx:DecafParser.While_statementContext):
        pass


    # Enter a parse tree produced by DecafParser#return_statement.
    def enterReturn_statement(self, ctx:DecafParser.Return_statementContext):
        pass

    # Exit a parse tree produced by DecafParser#return_statement.
    def exitReturn_statement(self, ctx:DecafParser.Return_statementContext):
        pass


    # Enter a parse tree produced by DecafParser#method_statement.
    def enterMethod_statement(self, ctx:DecafParser.Method_statementContext):
        pass

    # Exit a parse tree produced by DecafParser#method_statement.
    def exitMethod_statement(self, ctx:DecafParser.Method_statementContext):
        pass


    # Enter a parse tree produced by DecafParser#block_statement.
    def enterBlock_statement(self, ctx:DecafParser.Block_statementContext):
        pass

    # Exit a parse tree produced by DecafParser#block_statement.
    def exitBlock_statement(self, ctx:DecafParser.Block_statementContext):
        pass


    # Enter a parse tree produced by DecafParser#assign_statement.
    def enterAssign_statement(self, ctx:DecafParser.Assign_statementContext):
        pass

    # Exit a parse tree produced by DecafParser#assign_statement.
    def exitAssign_statement(self, ctx:DecafParser.Assign_statementContext):
        pass


    # Enter a parse tree produced by DecafParser#char_assign_statement.
    def enterChar_assign_statement(self, ctx:DecafParser.Char_assign_statementContext):
        pass

    # Exit a parse tree produced by DecafParser#char_assign_statement.
    def exitChar_assign_statement(self, ctx:DecafParser.Char_assign_statementContext):
        pass


    # Enter a parse tree produced by DecafParser#expression_statement.
    def enterExpression_statement(self, ctx:DecafParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by DecafParser#expression_statement.
    def exitExpression_statement(self, ctx:DecafParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by DecafParser#single_location.
    def enterSingle_location(self, ctx:DecafParser.Single_locationContext):
        pass

    # Exit a parse tree produced by DecafParser#single_location.
    def exitSingle_location(self, ctx:DecafParser.Single_locationContext):
        pass


    # Enter a parse tree produced by DecafParser#array_location.
    def enterArray_location(self, ctx:DecafParser.Array_locationContext):
        pass

    # Exit a parse tree produced by DecafParser#array_location.
    def exitArray_location(self, ctx:DecafParser.Array_locationContext):
        pass


    # Enter a parse tree produced by DecafParser#int_literal_expression.
    def enterInt_literal_expression(self, ctx:DecafParser.Int_literal_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#int_literal_expression.
    def exitInt_literal_expression(self, ctx:DecafParser.Int_literal_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#not_expression.
    def enterNot_expression(self, ctx:DecafParser.Not_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#not_expression.
    def exitNot_expression(self, ctx:DecafParser.Not_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#rel_op_expression.
    def enterRel_op_expression(self, ctx:DecafParser.Rel_op_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#rel_op_expression.
    def exitRel_op_expression(self, ctx:DecafParser.Rel_op_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#methodCall_expression.
    def enterMethodCall_expression(self, ctx:DecafParser.MethodCall_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#methodCall_expression.
    def exitMethodCall_expression(self, ctx:DecafParser.MethodCall_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#var_location_expression.
    def enterVar_location_expression(self, ctx:DecafParser.Var_location_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#var_location_expression.
    def exitVar_location_expression(self, ctx:DecafParser.Var_location_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#eq_op_expression.
    def enterEq_op_expression(self, ctx:DecafParser.Eq_op_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#eq_op_expression.
    def exitEq_op_expression(self, ctx:DecafParser.Eq_op_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#negative_expression.
    def enterNegative_expression(self, ctx:DecafParser.Negative_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#negative_expression.
    def exitNegative_expression(self, ctx:DecafParser.Negative_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#char_literal_expression.
    def enterChar_literal_expression(self, ctx:DecafParser.Char_literal_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#char_literal_expression.
    def exitChar_literal_expression(self, ctx:DecafParser.Char_literal_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#bool_literal_expression.
    def enterBool_literal_expression(self, ctx:DecafParser.Bool_literal_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#bool_literal_expression.
    def exitBool_literal_expression(self, ctx:DecafParser.Bool_literal_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_expression.
    def enterArith_expression(self, ctx:DecafParser.Arith_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_expression.
    def exitArith_expression(self, ctx:DecafParser.Arith_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#cond_op_expression.
    def enterCond_op_expression(self, ctx:DecafParser.Cond_op_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#cond_op_expression.
    def exitCond_op_expression(self, ctx:DecafParser.Cond_op_expressionContext):
        pass


    # Enter a parse tree produced by DecafParser#parens_expression.
    def enterParens_expression(self, ctx:DecafParser.Parens_expressionContext):
        pass

    # Exit a parse tree produced by DecafParser#parens_expression.
    def exitParens_expression(self, ctx:DecafParser.Parens_expressionContext):
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


