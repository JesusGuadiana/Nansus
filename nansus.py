# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language Parser
#  Last edit: 14/11/2018
# -----------------------------------------------------------------------------
from ply import *
from structures.funcDirectory import *
from structures.quad import *
from structures.semCube import *
from structures.funcDirectory import *
from currentProgram import CurrentProgram
from functions.gotoMain import goto_main_quad
from functions.addVariable import add_variable_to_directory
from functions.pushOperand import push_operand_to_stack
from functions.evaluateAssign import evaluate_assignment
from functions.evaluateOperation import evaluate_operation
from functions.pushConstant import push_constant_to_stack
import lex
import sys

tokens = lex.tokens
current_program = CurrentProgram()

#Default syntax error message
def p_error(p):
	print("Syntax error at %s" %p.value)

#Program Syntax Diagram Representaion
def p_program(p):
	'program : PRGM ID main_quad add_program_function EOS program_prime'

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
	goto_main_quad(current_program.quad_number, current_program.quad_list);
	current_program.quad_number += 1

def p_add_program_function(p):
	'''add_program_function : '''
	current_program.scope_g = p[-2]
	current_program.scope_l = p[-2]
	current_program.func_directory.new_function(current_program.scope_g, 'void')

#Vars Syntax Diagram Representation
def p_vars(p):
	'''vars : type vars_prime vars_fourth_prime '''

def p_vars_prime(p):
	'vars_prime : ID save_id vars_second_prime'

#Useful information for persistent current evaluated id
def p_save_id(p):
	'save_id : '
	current_program.current_id = p[-1]

def p_vars_second_prime(p):
	'''vars_second_prime : change_dimension LEFTB exp RIGHTB vars_third_prime
						| '''
	
#Flag changer for a dimensioned variable
def p_change_dimension(p):
	'change_dimension : '
	current_program.current_dim = 1

def p_vars_third_prime(p):
	'''vars_third_prime : LEFTB exp RIGHTB
			   | '''

def p_vars_fourth_prime(p):
	'''vars_fourth_prime : SEPARATOR store_variable vars_prime vars_fourth_prime
				   | store_variable vars_fifth_prime'''

#Adds the variable to the funcDirectory in the current function
def p_store_variable(p):
	'store_variable : '
	add_variable_to_directory(current_program)
	current_program.current_dim = 0

def p_vars_fifth_prime(p):
	'vars_fifth_prime : EOS'


#Type Syntax Diagram Representation
def p_type(p):
	'''type : TYPEINT
			| TYPEFLOAT
			| TYPECHAR'''

	current_program.current_type = p[1]

#Body Syntax Diagram Representation
def p_body(p):
	'''body : statement EOS body_prime'''

def p_body_prime(p):
	'''body_prime : body
				   | '''


#Module Syntax Diagram Representation
def p_modules(p):
	'''modules : FUNCTION modules_prime ID LEFTP era_quad modules_second_prime'''

def p_modules_prime(p):
	'''modules_prime : type
				   | NOTYPE void_type'''

def p_void_type(p):
	'void_type : '
	current_program.current_type = "void"

def p_modules_second_prime(p):
	'modules_second_prime : type ID modules_third_prime'

def p_modules_third_prime(p):
	'''modules_third_prime : SEPARATOR modules_second_prime
				   | RIGHTP LEFTBRACE modules_fourth_prime'''

def p_modules_fourth_prime(p):
	'''modules_fourth_prime : vars modules_fourth_prime
							| body RIGHTBRACE'''

def p_era_quad(p):
	era_quad()
	quad_number += 1



#Stack Pushing commands
def p_push_operand(p):
	'push_operand : '
	push_operand_to_stack(current_program, p[-1]);
	current_program.current_dim = 1

def p_push_operator(p):
	'push_operator : '
	current_program.operator_stack.append(p[-1])

#Statement Syntax Diagram Representation
def p_statement(p):
	'''statement : assignment
			| print
			| functioncall
			| condition
			| specialfunction'''


#Increment Syntax Diagram Representation
def p_increment(p):
	'increment : ID increment_prime'

def p_increment_prime(p):
	'''increment_prime : EQUALS increment_second_prime
				   | INCREMENT'''

def p_increment_second_prime(p):
	'''increment_second_prime : CSTI PLUS ID
				   | ID PLUS CSTI'''


#Assignment Syntax Diagram Representation
def p_assignment(p):
	'assignment : ID assignment_prime EQUALS push_operator expression'

def p_assignment_prime(p):
	'''assignment_prime : 
				   | LEFTB exp RIGHTB assignment_second_prime'''

def p_assignment_second_prime(p):
	'''assignment_second_prime : 
				   | LEFTB exp RIGHTB'''
	current_program.current_dim = 1

def p_eval_assignment(p):
	'eval_assignment : '
	evaluate_assignment(current_program)
	current_program.quad_number += 1


#Condition Syntax Diagram Representation
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


#Functioncall Syntax Diagram Representation
def p_functioncall(p):
	'functioncall : ID LEFTP fake_bottom exp functioncall_prime'

def p_functioncall_prime(p):
	'''functioncall_prime : SEPARATOR exp functioncall_prime
					| RIGHTP pop_fake_bottom'''


#Expression Syntax Diagram Representation
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


#Print Syntax Diagram Representation
def p_print(p):
	'print : PRINT LEFTP print_prime'

def p_print_prime(p):
	'''print_prime : RIGHTP
					| expression RIGHTP'''


#Exp Syntax Diagram Representation
def p_exp(p):
	'exp : term exp_prime'

def p_exp_prime(p):
	'''exp_prime : PLUS term exp_prime
					| MINUS term exp_prime
					| '''


#Operand Syntax Diagram Representation
def p_operand(p):
	'''operand : CSTI evaluate_operation_int
			| CSTF evaluate_operation_float
			| ID operand_prime'''

def p_evaluate_operation_int(p):
	'evaluate_operation_int : '
	push_constant_to_stack(current_program, p[-1], 'int')

def p_evaluate_operation_float(p):
	'evaluate_operation_float : '
	push_constant_to_stack(current_program, p[-1], 'float')

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


#Term Syntax Diagram Representation
def p_term(p):
	'term : factor term_prime'

def p_term_prime(p):
	'''term_prime : MULTIPLY factor term_prime
			| DIVIDE factor term_prime
			| '''

#Factor Syntax Diagram Representation
def p_factor(p):
	'''factor : LEFTP fake_bottom expression RIGHTP pop_fake_bottom
			| operand
			| PLUS operand
			| MINUS operand'''

def p_fake_bottom(p):
	'fake_bottom : '
	current_program.operator_stack.append('[(')

def p_pop_fake_bottom(p):
	'pop_fake_bottom : '
	current_program.operator_stack.pop()


#SpecialFunction Syntax Diagram Representation
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


#Compoundexp Syntax Diagram Representation
def p_compoundexp(p):
	'compoundexp : expression compoundexp_prime'

def p_compoundexp_prime(p):
	'''compoundexp_prime : AND compoundexp
			| OR compoundexp
			| '''

#Executes parser
import ply.yacc as yacc
import pprint
parser = yacc.yacc()

pp = pprint.PrettyPrinter(indent=4)
with open('test.txt','r') as f:
	input = f.read()
pp.pprint(parser.parse(input))