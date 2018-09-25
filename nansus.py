# -----------------------------------------------------------------------------
# nansus.py
#
#  Nando and Jesus’ Programming Language
# -----------------------------------------------------------------------------
# Build the lexer
import ply.lex as lex

tokens = ( "ID", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "CSTI","CSTF", "PRGM", "MAIN", "END", "FUNCTION", "EOS","LEFTP", "RIGHTP", "LEFTB", "RIGHTB", "WHILE", "FOR","IF", "ELSE", "ELSEIF", "PRINT", "NOT", "AND", "OR", "JEDO","CIRCLE", "SQUARE", "RECTANGLE", "FORWARD", "BACK", "TURNRIGHT", "TURNLEFT", "COLOR", "ARCH", "LINE", "THICKNESS","SEPARATOR", "POINT", "EQUALS", "TYPEINT", "TYPEFLOAT", "TYPECHAR", "STRING", "NOTYPE", "GREATER", "GREATEREQUAL","LESS", "LESSEQUAL", "EQUAL", "NOTEQUAL" )

# Tokens
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE =  r'/'
t_CSTI = r'\d+'
t_CSTF = r'\d*\.\d+'
t_PRGM = r'program'
t_MAIN = r'main'
t_END = r'end'
t_FUNCTION = r'function'
t_WHILE = r'while'
t_FOR = r'for'
t_IF = r'if'
t_ELSE = r'else'
t_ELSEIF = r'elseif'
t_PRINT = r'print'
t_EOS = r'\;'
t_LEFTP = r'\('
t_RIGHTP = r'\)'
t_LEFTB = r'\['
t_RIGHTB = r'\]'
t_NOT = r'\!'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_JEDO = r'jedo'
t_CIRCLE = r'circle'
t_SQUARE = r'square'
t_RECTANGLE = r'rectangle'
t_FORWARD = r'forward'
t_BACK = r'back'
t_TURNRIGHT = r'turnRight'
t_TURNLEFT = r'turnLeft'
t_COLOR = r'color'
t_ARCH = r'arch'
t_LINE = r'line'
t_THICKNESS = r'thickness'
t_SEPARATOR = r'\,'
t_POINT = r'\.'
t_EQUALS = r'\='
t_TYPEFLOAT = r'float'
t_TYPECHAR = r'char'
t_STRING = r'\”.*\”'
t_NOTYPE = r'void'
t_GREATER = r'\>'
t_GREATEREQUAL = r'\>\='
t_LESS = r'\<'
t_LESSEQUAL = r'\<\='
t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
#TODO ALGO ESTA MAL CON ESTO
#t_TYPEINT = r'\int'

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

lexer = lex.lex()

# Parsing rules
precedence = ( ('left','PLUS','MINUS'),
 ('left','MULTIPLY','DIVIDE'),
 ('left','AND','OR'), )

 # dictionary of names
names = { }

def p_program(t):
    'program : PRGM ID vars modules MAIN body END'

def p_vars(t):
    'vars : type vars_prime vars_fourth_prime'

def p_vars_prime(t):
    'vars_prime : ID vars_second_prime'

def p_vars_second_prime(t):
    '''vars_second_prime : LEFTB exp RIGHTB vars_third_prime
			| empty'''

def p_vars_third_prime(t):
    '''vars_third_prime : LEFTB exp RIGHTB
		       | empty'''

def p_vars_fourth_prime(t):
	'''vars_fourth_prime : SEPARATOR vars_prime vars_fourth_prime
			       | EOS'''

def p_type(t):
	'''type : TYPEINT
	          | TYPEFLOAT
                      | TYPECHAR'''
def p_body(t):
    'body : statement EOS body_prime'

def p_body_prime(t):
	'''body_prime : body
		           | empty'''

def modules(t):
    'modules : FUNCTION modules_prime ID LEFTP modules_second_prime'

def p_modules_prime(t):
    '''modules_prime : type
		           | NOTYPE'''

def p_modules_second_prime(t):
    'modules_second_prime : type ID modules_third_prime'

def p_modules_third_prime(t):
    '''modules_third_prime : SEPARATOR modules_second_prime
		           | RIGHTP LEFTP vars body RIGHTP'''

def p_statement(t):
    '''statement : assignment
			| print
            | functioncall
            | condition
            | specialfunction'''

def p_increment(t):
    'increment : ID increment_prime'

def p_increment_prime(t):
    '''increment_prime : EQUALS increment_second_prime
		           | PLUS PLUS'''

def p_increment_second_prime(t):
    '''increment_second_prime : CSTI PLUS ID
		           | ID PLUS CSTI'''

def p_assignment(t):
    'assignment : ID assignment_prime EQUALS expression'

def p_assignment_prime(t):
    '''assignment_prime : empty
		           | LEFTB exp RIGHTB assignment'''

def p_assignment_second_prime(t):
    '''assignment_second_prime : empty
		           | LEFTB exp RIGHTB'''

def p_condition(t):
    '''condition : WHILE LEFTP compoundexp RIGHTP LEFTB body RIGHTB
                   | FOR LEFTP assignment condition_prime
                   | IF condition_second_prime'''

def p_condition_prime(t):
    '''condition_prime : SEPARATOR assignment condition_prime
                   | EOS compoundexp EOS increment RIGHTP LEFTB body RIGHTB'''

def p_condition_second_prime(t):
    'condition_second_prime : LEFTP compoundexp RIGHTP condition_third_prime'

def p_condition_third_prime(t):
    '''condition_third_prime : statement condition_fourth_prime
                    | LEFTB body RIGHTB condition_fourth_prime'''

def p_condition_fourth_prime(t):
    '''condition_fourth_prime : ELSEIF condition_second_prime
                    | ELSE condition_fifth_prime
                    | empty'''

def p_condition_fifth_prime(t):
    '''condition_fifth_prime : statement
                    | LEFTB body RIGHTB'''

def p_functioncall(t):
    'functioncall : ID LEFTP exp functioncall_prime'

def p_functioncall_prime(t):
    '''functioncall_prime : SEPARATOR exp functioncall_prime
                    | RIGHTP'''

def p_expression(t):
    'expression : exp expression_prime'

def p_expression_prime(t):
    '''expression_prime : exp expression_prime
                    | GREATER
                    | LESS
                    | EQUAL
                    | NOTEQUAL
                    | GREATEREQUAL
                    | LESSEQUAL
                    | empty'''

def p_print(t):
    'print : PRINT LEFTP print_prime'

def p_print_prime(t):
    '''print_prime : STRING RIGHTP
                    | expression RIGHTP'''

def p_exp(t):
    'exp : term exp_prime'

def p_exp_prime(t):
    '''exp_prime : PLUS term exp_prime
                    | MINUS term exp_prime
                    | empty'''

def p_operand(t):
    '''operand : CSTI
            | CSTF
            | ID operand_prime'''

def p_operand_prime(t):
    '''operand_prime : empty
            | LEFTB exp RIGHTB operand_second_prime
            | LEFTP exp operand_third_prime'''

def p_operand_second_prime(t):
    '''operand_second_prime : empty
            | LEFTB exp RIGHTB'''

def p_operand_third_prime(t):
    '''operand_third_prime : SEPARATOR exp operand_third_prime
            | RIGHTP'''

def p_term(t):
    'term : factor term_prime'

def p_term_prime(t):
    '''term_prime : MULTIPLY factor term_prime
            | DIVIDE factor term_prime
            | empty'''

def p_factor(t):
    '''factor : LEFTP expression RIGHTP
            | operand
            | PLUS operand
            | MINUS operand'''

def p_specialfunction(t):
    'specialfunction : JEDO POINT specialfunction_prime'

def p_specialfunction_prime(t):
    '''specialfunction_prime : CIRCLE LEFTP exp RIGHTP
            | SQUARE LEFTP exp SEPARATOR exp RIGHTP
            | RECTANGLE LEFTP exp SEPARATOR exp RIGHTP
            | FORWARD LEFTP exp RIGHTP
            | BACK LEFTP exp RIGHTP
            | TURNRIGHT LEFTP exp RIGHTP
            | TURNLEFT LEFTP exp RIGHTP
            | COLOR LEFTP exp SEPARATOR exp SEPARATOR exp RIGHTP
            | ARCH LEFTP exp RIGHTP
            | LINE LEFTP exp SEPARATOR exp RIGHTP
            | THICKNESS LEFTP exp RIGHTP'''

import ply.yacc as yacc
parser = yacc.yacc()

with open('prueba.txt','r') as f:
	input = f.read()
	pp.pprint(parser.parse(input))
