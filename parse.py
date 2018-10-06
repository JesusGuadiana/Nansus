from ply import *
import lex

tokens = lex.tokens

# Parsing rules
precedence = ( ('left','PLUS','MINUS'),
 ('left','MULTIPLY','DIVIDE'),
 ('left','AND','OR'), )

 # dictionary of names
names = { }
def p_error(p):
  print("Syntax error at %s"%p.value)

def p_program(p):
    'program : PRGM ID vars modules MAIN body END'

def p_vars(p):
    'vars : type vars_prime vars_fourth_prime'

def p_vars_prime(p):
    'vars_prime : ID vars_second_prime'

def p_vars_second_prime(p):
    '''vars_second_prime : LEFTB exp RIGHTB vars_third_prime
			| EMPTY'''

def p_vars_third_prime(p):
    '''vars_third_prime : LEFTB exp RIGHTB
		       | EMPTY'''

def p_vars_fourth_prime(p):
	'''vars_fourth_prime : SEPARATOR vars_prime vars_fourth_prime
			       | EOS'''

def p_type(p):
	'''type : TYPEINT
	          | TYPEFLOAT
                      | TYPECHAR'''
def p_body(p):
    'body : statement EOS body_prime'

def p_body_prime(p):
	'''body_prime : body
		           | EMPTY'''

def p_modules(p):
    'modules : FUNCTION modules_prime ID LEFTP modules_second_prime'

def p_modules_prime(p):
    '''modules_prime : type
		           | NOTYPE'''

def p_modules_second_prime(p):
    'modules_second_prime : type ID modules_third_prime'

def p_modules_third_prime(p):
    '''modules_third_prime : SEPARATOR modules_second_prime
		           | RIGHTP LEFTP vars body RIGHTP'''

def p_statement(p):
    '''statement : assignment
			| print
            | functioncall
            | condition
            | specialfunction'''

def p_increment(p):
    'increment : ID increment_prime'

def p_increment_prime(p):
    '''increment_prime : EQUALS increment_second_prime
		           | PLUS PLUS'''

def p_increment_second_prime(p):
    '''increment_second_prime : CSTI PLUS ID
		           | ID PLUS CSTI'''

def p_assignment(p):
    'assignment : ID assignment_prime EQUALS expression'

def p_assignment_prime(p):
    '''assignment_prime : EMPTY
		           | LEFTB exp RIGHTB assignment_second_prime'''

def p_assignment_second_prime(p):
    '''assignment_second_prime : EMPTY
		           | LEFTB exp RIGHTB'''

def p_condition(p):
    '''condition : WHILE LEFTP compoundexp RIGHTP LEFTB body RIGHTB
                   | FOR LEFTP assignment condition_prime
                   | IF condition_second_prime'''

def p_condition_prime(p):
    '''condition_prime : SEPARATOR assignment condition_prime
                   | EOS compoundexp EOS increment RIGHTP LEFTB body RIGHTB'''

def p_condition_second_prime(p):
    'condition_second_prime : LEFTP compoundexp RIGHTP condition_third_prime'

def p_condition_third_prime(p):
    '''condition_third_prime : statement condition_fourth_prime
                    | LEFTB body RIGHTB condition_fourth_prime'''

def p_condition_fourth_prime(p):
    '''condition_fourth_prime : ELSEIF condition_second_prime
                    | ELSE condition_fifth_prime
                    | EMPTY'''

def p_condition_fifth_prime(p):
    '''condition_fifth_prime : statement
                    | LEFTB body RIGHTB'''

def p_functioncall(p):
    'functioncall : ID LEFTP exp functioncall_prime'

def p_functioncall_prime(p):
    '''functioncall_prime : SEPARATOR exp functioncall_prime
                    | RIGHTP'''

def p_expression(p):
    'expression : exp expression_prime'

def p_expression_prime(p):
    '''expression_prime : exp expression_prime
                    | GREATER
                    | LESS
                    | EQUAL
                    | NOTEQUAL
                    | GREATEREQUAL
                    | LESSEQUAL
                    | EMPTY'''

def p_print(p):
    'print : PRINT LEFTP print_prime'

def p_print_prime(p):
    '''print_prime : STRING RIGHTP
                    | expression RIGHTP'''

def p_exp(p):
    'exp : term exp_prime'

def p_exp_prime(p):
    '''exp_prime : PLUS term exp_prime
                    | MINUS term exp_prime
                    | EMPTY'''

def p_operand(p):
    '''operand : CSTI
            | CSTF
            | ID operand_prime'''

def p_operand_prime(p):
    '''operand_prime : EMPTY
            | LEFTB exp RIGHTB operand_second_prime
            | LEFTP exp operand_third_prime'''

def p_operand_second_prime(p):
    '''operand_second_prime : EMPTY
            | LEFTB exp RIGHTB'''

def p_operand_third_prime(p):
    '''operand_third_prime : SEPARATOR exp operand_third_prime
            | RIGHTP'''

def p_term(p):
    'term : factor term_prime'

def p_term_prime(p):
    '''term_prime : MULTIPLY factor term_prime
            | DIVIDE factor term_prime
            | EMPTY'''

def p_factor(p):
    '''factor : LEFTP expression RIGHTP
            | operand
            | PLUS operand
            | MINUS operand'''

def p_specialfunction(p):
    'specialfunction : JEDO POINT specialfunction_prime'

def p_specialfunction_prime(p):
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

def p_compoundexp(p):
    'compoundexp : expression compoundexp_prime'

def p_compoundexp_prime(p):
    '''compoundexp_prime : AND compoundexp
            | OR compoundexp
            | EMPTY'''


import ply.yacc as yacc
parser = yacc.yacc()
