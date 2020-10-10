import sys
from antlr4 import *
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from miVisitor import miVisitor
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from graphviz import Digraph
from codigo_intermedio import *
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'
res = []

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DecafLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.program()
    
    visitor = miVisitor()
    visitor.visit(tree)
    
    simbolos = visitor.simb
    metodos = visitor.meto
    tipos = visitor.tip
    errores = visitor.errores
    
    
    codigo_inter = codigo_intermedio(tipos, metodos, simbolos)
    codigo_inter.visit(tree)
    
    #print(Trees.toStringTree(tree, None, parser))
    #arbol(tree, parser.ruleNames)
    
    
def arbol(tree, rule_names, indent = 0):
    if isinstance(tree, TerminalNodeImpl):
        res.append([indent, tree.getText()])
    else:
        res.append([indent, rule_names[tree.getRuleIndex()]])
        for child in tree.children:
            arbol(child, rule_names, indent + 1)
    
def graficadora(resultado, resp):
    f = Digraph('finite_state_machine', filename='./hsdoli.gv')
    f.attr(rankdir='TB', size='8,5')
    f.attr('node', shape='doublecircle')
    f.node(resultado[0][1])
    f.attr('node', shape='circle')
    holis = 1
    ##resp =4
    padre_actual = []
    padre_actual.append(0)
    o = 0

    for x in range(1, len(resultado)):
        if holis == resultado[x][0]:
            f.edge(resultado[padre_actual[o]][1], resultado[x][1])
            
        else:
            if resultado[x-1][0] > resultado[x][0]:

                holis -= resultado[x-1][0] - resultado[x][0]
                o-= resultado[x-1][0] - resultado[x][0]
                f.edge(resultado[padre_actual[o]][1], resultado[x][1])
            else:
                holis +=1
                padre_actual.append(x-1)
                o+=1
                f.edge(resultado[padre_actual[o]][1], resultado[x][1])
                
    f.view()

    

if __name__ == '__main__':
    
    maximo = 0
    main(sys.argv)

    for i in range(len(res)):
        if int(res[i][0]) >= maximo:
            maximo = res[i][0] 
    
    ##graficadora(res,maximo)