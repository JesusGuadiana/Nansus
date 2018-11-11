from ply import *
import lex
from Program import Program
from quadruple import Quadruple
import sys

current_program = Program()

tokens = lex.tokens

 # dictionary of names
names = { }

def p_error(p):
	print("Syntax error at %s" %p.value)

def p_program(p):
    'program : PRGM ID main_quad add_function_to_directory EOS program_prime'

def p_program_prime(p):
	'''program_prime : vars program_prime
					| program_second_prime'''

def p_program_second_prime(p):
	'''program_second_prime : modules program_second_prime
							| MAIN program_third_prime'''

def p_program_third_prime(p):
	'''program_third_prime : vars program_third_prime
							| body END'''

def p_main_quad(p):
	'''main_quad : '''
	current_quad = Quadruple(current_program.quad_num,'GOTO', 'MAIN', None, None)
	current_program.quad_list.append(current_quad)
	current_program.quad_num += 1
	print(current_quad)

def p_add_function_to_directory(p):
	'''add_function_to_directory : '''
	current_program.global_scope = p[-2]
	current_program.current_scope = p[-2]
	current_program.function_directory.add_function(current_program.global_scope, 'void')

def p_vars(p):
    '''vars : type type_getter vars_prime vars_fourth_prime '''

def p_type_getter(p):
	'''type_getter : '''

def p_vars_prime(p):
    'vars_prime : ID vars_second_prime'

def p_vars_second_prime(p):
    '''vars_second_prime : LEFTB exp RIGHTB vars_third_prime
    					| '''
    if p[-1] is not None:
    	variable_name = p[-1]
    	current_program.temp_variables.append(variable_name)

def p_vars_third_prime(p):
    '''vars_third_prime : LEFTB exp RIGHTB
		       | '''

def p_vars_fourth_prime(p):
	'''vars_fourth_prime : SEPARATOR vars_prime vars_fourth_prime
			       | vars_fifth_prime'''

def p_vars_fifth_prime(p):
	'vars_fifth_prime : EOS'
	variable_type = current_program.temp_type
	current_program.temp_variables.reverse()
	for variable in current_program.temp_variables:
		variable_declared = current_program.function_directory.check_variable_existance(current_program.current_scope, variable)
		if not variable_declared:
			if current_program.current_scope == current_program.global_scope:
				variable_address = current_program.memory.obtain_global_address(variable_type)
			else:
				variable_address = current_program.memory.obtain_local_address(variable_type)			
			current_program.function_directory.add_variable_to_function(current_program.current_scope, variable_type, variable, variable_address)
	del current_program.temp_variables[:]

def p_type(p):
	'''type : TYPEINT
			| TYPEFLOAT
			| TYPECHAR'''
	current_program.temp_type = p[1]

def p_body(p):
    '''body : statement EOS body_prime'''

def p_body_prime(p):
	'''body_prime : body
		           | '''

def p_modules(p):
    '''modules : FUNCTION modules_prime ID LEFTP modules_second_prime'''

def p_modules_prime(p):
    '''modules_prime : type
		           | NOTYPE'''

def p_modules_second_prime(p):
    'modules_second_prime : type ID modules_third_prime'

def p_modules_third_prime(p):
    '''modules_third_prime : SEPARATOR modules_second_prime
		           | RIGHTP LEFTBRACE modules_fourth_prime'''

def p_modules_fourth_prime(p):
	'''modules_fourth_prime : vars modules_fourth_prime
							| body RIGHTBRACE'''

#Push el id a la pila operandos 
def p_push_to_operandstack(p):
	'''push_to_operandstack	: 
	'''
	variable = current_program.function_directory.get_function_variable(current_program.current_scope, p[-1])
	if variable is None:
		variable = current_program.function_directory.get_function_variable(current_program.global_scope, p[-1])
		if variable is None:
			print("The variable " + p[-1] + " was not defined for this function.")
			sys.exit()
		else:
			current_program.operand_stack.append(variable['memory_address'])
			current_program.type_stack.append(variable['type'])
	else:
		current_program.operand_stack.append(variable['memory_address'])
		current_program.type_stack.append(variable['type'])

#Push el operador al pila operadores
def p_push_to_operatorstack(p):
	'''push_to_operatorstack	: 
	'''
	current_program.operator_stack.append(p[-1])

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
		           | INCREMENT'''

def p_increment_second_prime(p):
    '''increment_second_prime : CSTI PLUS ID
		           | ID PLUS CSTI'''

def p_assignment(p):
    'assignment : ID push_to_operandstack assignment_prime EQUALS push_to_operatorstack expression assign_quads'

def p_assignment_prime(p):
    '''assignment_prime : 
		           | LEFTB exp RIGHTB assignment_second_prime'''

def p_assignment_second_prime(p):
    '''assignment_second_prime : 
		           | LEFTB exp RIGHTB'''

def p_assign_quads(p):
	'''assign_quads	: 
	'''
	operator = current_program.operator_stack.pop()
	if operator == '=':
		right_operand = current_program.operand_stack.pop()
		right_type = current_program.type_stack.pop()
		left_operand = current_program.operand_stack.pop()
		left_type = current_program.type_stack.pop()
		result_type = current_program.semantic_cube.get_semantic_type(left_type, right_type, operator)
		if result_type != 'error':
			quadruple = Quadruple(current_program.quad_num, operator, right_operand, None, left_operand)
			current_program.quad_list.append(quadruple)
			current_program.quad_num += 1
		else:
			print('Operation type mismatch at {0}'.format(p.lexer.lineno))
			sys.exit()

def p_condition(p):
    '''condition : WHILE LEFTP compoundexp RIGHTP LEFTBRACE body RIGHTBRACE
                   | FOR LEFTP assignment condition_prime
                   | IF condition_second_prime'''

def p_condition_prime(p):
    '''condition_prime : SEPARATOR assignment condition_prime
                   | EOS compoundexp EOS increment RIGHTP LEFTBRACE body RIGHTBRACE'''

def p_condition_second_prime(p):
    'condition_second_prime : LEFTP compoundexp RIGHTP condition_third_prime'

def p_condition_third_prime(p):
    '''condition_third_prime : statement condition_fourth_prime
                    | LEFTBRACE body RIGHTBRACE condition_fourth_prime'''

def p_condition_fourth_prime(p):
    '''condition_fourth_prime : ELSEIF condition_second_prime
                    | ELSE condition_fifth_prime
                    | '''

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
    '''expression_prime : GREATER exp expression_prime
                    | LESS exp expression_prime
                    | EQUAL exp expression_prime
                    | NOTEQUAL exp expression_prime
                    | GREATEREQUAL exp expression_prime
                    | LESSEQUAL exp expression_prime
                    | '''

def p_print(p):
    'print : PRINT LEFTP print_prime'

def p_print_prime(p):
    '''print_prime : RIGHTP
                    | expression RIGHTP'''

def p_exp(p):
    'exp : term exp_prime'

def p_exp_prime(p):
    '''exp_prime : PLUS term exp_prime
                    | MINUS term exp_prime
                    | '''

def p_operand(p):
    '''operand : CSTI
            | CSTF
            | ID operand_prime'''

def p_operand_prime(p):
    '''operand_prime : LEFTB exp RIGHTB operand_second_prime
            | LEFTP exp operand_third_prime
            | '''

def p_operand_second_prime(p):
    '''operand_second_prime : 
            | LEFTB exp RIGHTB'''

def p_operand_third_prime(p):
    '''operand_third_prime : SEPARATOR exp operand_third_prime
            | RIGHTP'''

def p_term(p):
    'term : factor term_prime'

def p_term_prime(p):
    '''term_prime : MULTIPLY factor term_prime
            | DIVIDE factor term_prime
            | '''

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
            | '''


import ply.yacc as yacc
import pprint
parser = yacc.yacc()
pp = pprint.PrettyPrinter(indent=4)

with open('prueba.txt','r') as f:
    input = f.read()
    pp.pprint(parser.parse(input))

