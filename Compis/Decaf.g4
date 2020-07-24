grammar Decaf;

@lexer::namespace{CustomIde}
@parser::namespace{CustomIde}

program 
	:   'class' Id '{' (declaration)* '}'
	;

declaration 
	:   structDeclaration
	|   varDeclaration
	|   methodDeclaration
	;
	 
varDeclaration 
	:   varType Id ';'												
	|   varType Id '[' Num ']' ';'									
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
	:   'int' Id '(' (parameter (',' parameter)*)? ')' block		
	|   'char' Id '(' (parameter (',' parameter)*)? ')' block		
	|   'boolean' Id '(' (parameter (',' parameter)*)? ')' block	
	|   'void' Id '(' (parameter (',' parameter)*)? ')' block		
	;

parameter
	:   parameterType Id		 #single_parameterDeclaration
	;

parameterType
	:   'int'					#int_parameterType
	|   'char'					#char_parameterType
	|   'boolean'				#boolean_parameterType
	;

block
	:   '{' (varDeclaration)* (statement)* '}' 
	;
statement
	:   'if' '(' expression ')' block ('else' block)?				
	|   'while' '(' expression ')' block							
	|   'return' (expression)? ';'									
	|   methodCall ';'												
	|   block														
	|   location '=' expression ';'									
	|   location '=' '(char)' expression ';'						
	|   (expression)? ';'											
	;

location  
	: Id ('.' location)?											
	|   Id '[' expression ']' ('.' location)?						
	;


expression  //ya
	:   location													
	|   methodCall													
	|	Num															
	|   CharacterLiteral											
	|   bool_literal												
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
	
arith_op
	:   '+'
	|   '-'
	|   '*'
	|   '/'
	|   '%'
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