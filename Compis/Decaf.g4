grammar Decaf;

@lexer::namespace{CustomIde}
@parser::namespace{CustomIde}

program 
	:   'class' Id '{' (declaration)* '}'
	;

declaration 
	:   structDeclaration#structDeclara
	|   varDeclaration#varDecla
	|   methodDeclaration#methodDecla
	;
	 
varDeclaration 
	:vartype=varType Id ';'#normal										
	|vartype= varType  Id '[' Num ']' ';'#lista
								
	;

structDeclaration
	:   'struct' Id '{' (varDeclaration)* '}' 
	;



varType
	:   'int'														
	|   'char'														
	|   'boolean'													
	|   'struct' Id												
	|   structDeclaration											
	|   'void'														
	;

methodDeclaration
	:   metoInt='int' Id '(' (parameter (',' parameter)*)? ')' block #metoInt		
	|   metoChar='char' Id '(' (parameter (',' parameter)*)? ')' block #metoChar		
	|   metoBool='boolean' Id '(' (parameter (',' parameter)*)? ')' block	#metoBool
	|   metVoid = 'void' Id '(' (parameter (',' parameter)*)? ')' block	#metoVoid	
	;

parameter
	:   param = parameterType Id#single_parameterDeclaration
	;

parameterType
	:   'int'#int_parameterType
	|   'char'#char_parameterType
	|   'boolean'#boolean_parameterType
	;

block
	:   '{'(varDeclaration)* (statement)* '}' 
	;


statement
   	:   ifStmt
	|   whileStmt
	|   returnStmt
	|   methodCall 	';'										
	|   block														
	|   location '=' expression';'							
	|   location '=' '(char)' expression ';'						
	|   (expression)? ';'										
	;

ifStmt
	:'if' '(' expression ')' block ('else' block)?
	;
whileStmt
	:'while' '(' expression ')' block
	;
returnStmt
	:'return' (expression)? ';'	
	;
location  
	: Id ('.' location)?										
	| Id '[' expression ']' ('.' location)?						
	;


expression  //ya
	:   location													
	|   methodCall													
	|   Num															
	|   CharacterLiteral											
	|   bool_literal
	|   expression arith_higher_op expression												
	|   expression arith_op expression								
	|   expression rel_op expression								
	|   expression eq_op expression									
	|   expression cond_op expression								
	|   '-' expression												
	|   '!' expression												
	|   '(' expression ')'											
	;

methodCall
	:	Id '(' (arg (',' arg)*)? ')' //ya
	;

arg
	:   expression //ya
	;

arith_higher_op
    : '*' 
    | '/' 
    | '%' 
    ;

arith_op
	:   '+'
	|   '-'
	;

rel_op
	:   '<'
	|   '>'
	|   '<='
	|   '>='
	;

eq_op
	:   '=='
	|   '!='
	;

cond_op
	:   '&&'
	|   '||'
	;
	
bool_literal //ya
	:   'true'
	|   'false'
	;

Id
	:   Letter (Letter|Digit)*
	;

Num
	:   Digit+
	;

CharacterLiteral
	:   '\'' SingleCharacter '\''
	;

fragment
SingleCharacter
	:   ~['\\]
	;

Digit 
	:   [0-9]
	;

Letter
	:   [a-zA-Z]
	;

WS  :   [  \t\r\n\u000C]+ -> skip ;
 
COMMENT
	:   '/*' .*? '*/' -> skip
	;

LINE_COMMENT
	:   '//' ~[\r\n]* -> skip
	;