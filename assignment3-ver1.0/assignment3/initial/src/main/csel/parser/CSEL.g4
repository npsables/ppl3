grammar CSEL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text[1:])
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result.text;
}

options{
	language=Python3;
}


program : manydecls+ EOF;

manydecls : vardecl_stmt | funcdecl | constant_decl;

constant_decl : CONSTANT var_constant  (CM var_constant)* SM;

funcdecl : FUNCTION NORM_ID LB paralist? RB block_stmt;

vardecl_stmt: LET var_temp  (CM var_temp)* SM;

var_temp: NORM_ID index_operators?  (COLON primtypes)? (ASSIGN exp_0)?;

var_constant: CONST_ID index_operators? (COLON primtypes)? (ASSIGN exp_0)?;

paralist : paradecl (CM paradecl)*;

paradecl : NORM_ID | CONST_ID | indexdecl;

exp_0: exp_1 STR_ADD exp_1
    | exp_1 STR_COMPARE exp_1
    | exp_1;
exp_1: exp_2 EQ exp_2
    | exp_2 NEQ exp_2
    | exp_2 LT exp_2
    | exp_2 GT exp_2
    | exp_2 LTEQ exp_2
    | exp_2 GTEQ exp_2
    | exp_2;
exp_2: exp_2 OR exp_3
    | exp_2 AND exp_3
    | exp_3;
exp_3: exp_3 ADD exp_4
    | exp_3 SUB exp_4
    | exp_4;
exp_4: exp_4 MUL exp_5
    | exp_4 DIV exp_5
    | exp_4 MOD exp_5
    | exp_5;
exp_5: NOT exp_5 | exp_6;
exp_6: SUB exp_6 | exp_7;
exp_7: exp_7 index_operators | exp_7 key_operators+| exp_8 ;
exp_8: LB exp_0 RB | operands;

index_operators: LS exp_0 (CM exp_0)* RS; //

key_operators: LP exp_0 RP ;

operands: NUMBER_LIT | funcalls | NORM_ID | CONST_ID
    | BOOLEAN_LIT | STRINGLIT | array_lit | json_lit ;

// statement

assign_stmt: lhs ASSIGN exp_0 SM;

lhs: NORM_ID | CONST_ID | exp_7;

if_stmt: IF LB exp_0 RB block_stmt (ELIF LB exp_0 RB block_stmt)* (ELSE  block_stmt)?;

while_stmt: WHILE LB exp_0 RB block_stmt;

for_stmt: forin_stmt | forof_stmt;

forin_stmt: FOR NORM_ID IN exp_0 block_stmt;

forof_stmt:  FOR NORM_ID OF exp_0 block_stmt;

break_stmt: BREAK SM;

continue_stmt: CONTINUE SM;

return_stmt: RETURN exp_0? SM;

funcalls: CALL LB NORM_ID CM (LS (exp_0 (CM exp_0)*)? RS) RB;

block_stmt: LP stmt* RP ;

stmt: constant_decl | vardecl_stmt| assign_stmt | if_stmt | for_stmt | while_stmt | break_stmt | continue_stmt | return_stmt | funcalls SM ;

// SPECIAL ONE
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// skip comment lines
COMMENT_LINES: '##' .*? '##' -> skip;
// the fuck? test lแบกi ## ##

// skip comment line
//LINE_COMMENT: '##' (~'\n'*) ('\n' '#' (~['\n''##']*) '\n') * '\n'? '##'  -> skip;

//
//FUNC_ID: [a-z][_a-zA-Z0-9]*;

NORM_ID: [a-z][_a-zA-Z0-9]* ;
CONST_ID: DOLLAR [a-z][_a-zA-Z0-9]*;
indexdecl:(NORM_ID | CONST_ID) (index_operators| LS RS);

json_lit: LP  WS* listkeyvalue  WS* RP;

//LITERALS
NUMBER_LIT: '-'?[0-9]*'.'([0-9]*)?([Ee]'-'?[0-9]+)? | '-'?[0-9]+'.'| '-'?[0-9]+[Ee]'-'?[0-9]+ | '-'?[0-9]+;
BOOLEAN_LIT: TRUE | FALSE;

DOLLAR: '$';
listkeyvalue: NORM_ID  WS* COLON  WS* normal_lit  ( WS* CM  WS* NORM_ID  WS* COLON  WS* normal_lit)*;
fragment STRINGCHARS: ~[\b\f\r\n\t'"\\] | ('\'"') ;
fragment ESCAPECASE: '\\'[tbfrn'"\\];
fragment LISTKEY: NUMBER_LIT (WS* CM WS* NUMBER_LIT)* | STRINGLIT (WS* CM WS* STRINGLIT)*;
STRINGLIT: '"'(STRINGCHARS|ESCAPECASE)* '"'{self.text = self.text[1:-1]};
array_lit: LS normal_lit (WS* CM WS* normal_lit)* RS;

normal_lit: NUMBER_LIT | BOOLEAN_LIT | array_lit | json_lit | STRINGLIT;

primtypes: STRING | NUMBER | JSON | ARRAY | BOOLEAN;

//OPERATORS
ADD: '+';
MUL: '*';
NOT: '!';
OR: '||';
NEQ: '!=';
LT: '<';
LTEQ: '<=';
ASSIGN: '=';
SUB: '-';
DIV: '/';
MOD: '%';
AND: '&&';
EQ: '==';
GT: '>';
GTEQ: '>=';
STR_ADD: '+.';
STR_COMPARE: '==.';


//SEPARATORS
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
SM: ';';
CM: ',';
LS: '[';
RS: ']';
DOT: '.';
COLON: ':';

// Keywords
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSE: 'Else';
ELIF: 'Elif';
WHILE:'While';
FOR: 'For';
OF: 'Of';
IN: 'In';
LET: 'Let';
TRUE: 'True';
FALSE: 'False';
CALL: 'Call';
NUMBER: 'Number';
BOOLEAN: 'Boolean';
STRING: 'String';
JSON: 'JSON';
CONSTANT: 'Constant';
RETURN: 'Return';
FUNCTION: 'Function';
ARRAY: 'Array';


UNCLOSE_STRING: '"'(STRINGCHARS|ESCAPECASE)*;
ILLEGAL_ESCAPE: '"'(STRINGCHARS|ESCAPECASE)* '\\' ~[tbfrn'"\\];
UNTERMINATED_COMMENT: '##' .*? ;
ERROR_CHAR: .;