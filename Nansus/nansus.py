# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  nansus.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
#Python Lexer & Yacc
from ply import *

#Main Program Structure Import
from currentProgram import CurrentProgram

#Structure imports
from structures.funcDirectory import FuncDirectory
from structures.quad import Quad
from structures.semCube import SemanticCube

#Function imports
from functions.addModules import add_module_to_directory
from functions.addParameter import add_parameter_to_function
from functions.addVariable import add_variable_to_directory
from functions.eraQuad import era_quad
from functions.evaluateAssign import evaluate_assignment
from functions.evaluateExpression import evaluate_binary_operation
from functions.evaluateOperation import evaluate_operation
from functions.functionReturn import return_from_function
from functions.gosubQuad import gosub_quad
from functions.noArgumentSpecialFunction import no_argument_special_function
from functions.oneArgumentSpecialFunction import one_argument_special_function
from functions.paramQuad import param_quad
from functions.printToOutputFile import print_to_output_file
from functions.pushConstant import push_constant_to_stack
from functions.pushId import push_id_to_stack
from functions.quadGenerator import quad_append
from functions.twoArgumentSpecialFunction import two_argument_special_function
from functions.threeArgumentSpecialFunction import three_argument_special_function

#Import Lexer and System Functions
import lex
import sys

#Obtain Tokens and Instantiate the Program Structure
tokens = lex.tokens
current_program = CurrentProgram()

#Default syntax error message
def p_error(p):
	print("Syntax error at %s" %p.value)






#Program Syntax Diagram Grammar Representation
def p_program(p):
	'program : PRGM ID main_quad add_program_function EOS program_prime'

def p_program_prime(p):
	'''program_prime : vars program_prime
					| modules program_prime
					| program_second_prime'''

def p_program_second_prime(p):
	'''program_second_prime : MAIN fill_main LEFTBRACE program_third_prime'''

def p_program_third_prime(p):
	'''program_third_prime : vars program_third_prime
							| body RIGHTBRACE EOS'''


#Calls function to create the default GOTO MAIN quadruple (First Action)
def p_main_quad(p):
	'main_quad : '
	print_to_output_file("\nINTERMEDIATE CODE: \n")
	current_program.quad_number += quad_append(current_program, Quad(current_program.quad_number, "GOTO", "MAIN", None, None))

#Calls function to add the program function to the function directory (Second Action)
def p_add_program_function(p):
	'add_program_function : '
	current_program.scope_g = p[-2]
	current_program.scope_l = p[-2]
	current_program.func_directory.new_function(current_program.scope_g, 'void')

def p_fill_main(p):
	'fill_main : '
	quad = current_program.quad_list[0]
	quad.set_quad_goto(current_program.quad_number)
	current_program.scope_l = p[-1]
	current_program.func_directory.new_function(current_program.scope_l, 'void')





#Vars Syntax Diagram Grammar Representation
def p_vars(p):
	'vars : type vars_prime vars_fourth_prime '

def p_vars_prime(p):
	'vars_prime : ID save_id vars_second_prime'

def p_vars_second_prime(p):
	'''vars_second_prime : change_dimension LEFTB exp RIGHTB first_dimension vars_third_prime
						| '''

def p_first_dimension(p):
	'first_dimension : '
	exp_type = current_program.type_stack.pop()
	if exp_type == 'int':
		result = current_program.operand_stack.pop()
		current_program.vec_mat_first_dimension = result
		current_program.func_directory.set_local_variable_dimension_one(
			current_program.scope_l, current_type, result)
	else:
		print("Type mismatch at condition.")
		sys.exit()

def p_vars_third_prime(p):
	'''vars_third_prime : LEFTB exp RIGHTB second_dimension dimensional_address_allocation
			   | dimensional_address_allocation'''

def p_second_dimension(p):
	'second_dimension : '
	exp_type = current_program.type_stack.pop()
	if exp_type == 'int':
		result = current_program.operand_stack.pop()
		current_program.vec_mat_second_dimension = result
	else:
		print("Type mismatch at condition.")

def p_dimensional_address_allocation(p):
	'dimensional_address_allocation : '
	add_vector_or_matrix

def p_vars_fourth_prime(p):
	'''vars_fourth_prime : SEPARATOR store_variable vars_prime vars_fourth_prime
				   | store_variable vars_fifth_prime'''

def p_vars_fifth_prime(p):
	'vars_fifth_prime : EOS'


#Save the id name in the global structure for easy usage (not an actual action)
def p_save_id(p):
	'save_id : '
	current_program.current_id = p[-1]

#Change flag for dimensioned variable within the main program structure
def p_change_dimension(p):
	'change_dimension : '
	current_program.vec_mat_variable_flag = True

#Adds the variable to the funcDirectory in the current function (Action 1)
def p_store_variable(p):
	'store_variable : '
	if not current_program.vec_mat_variable_flag:
		add_variable_to_directory(current_program)
	current_program.vec_mat_variable_flag = False






#Type Syntax Diagram Representation
def p_type(p):
	'''type : TYPEINT
			| TYPEFLOAT
			| TYPECHAR'''

	#Changes the current type for variable analysis (Action 1)
	current_program.current_type = p[1]






#Body Syntax Diagram Representation
def p_body(p):
	'body : statement body_prime'

def p_body_prime(p):
	'''body_prime : body
				   | '''






#Module Syntax Diagram Representation
def p_modules(p):
	'modules : FUNCTION modules_prime ID add_module LEFTP modules_second_prime'

def p_modules_prime(p):
	'''modules_prime : type
				   | NOTYPE void_type'''

def p_modules_second_prime(p):
	'modules_second_prime : type ID add_parameter modules_third_prime'

def p_modules_third_prime(p):
	'''modules_third_prime : SEPARATOR modules_second_prime
				   | RIGHTP LEFTBRACE modules_fourth_prime'''

def p_modules_fourth_prime(p):
	'''modules_fourth_prime : vars modules_fourth_prime
							| body modules_fifth_prime'''

def p_modules_fifth_prime(p):
	'''modules_fifth_prime : RETURN exp return_quad EOS RIGHTBRACE endproc_quad
							| RIGHTBRACE endproc_quad'''


#Sets the current type to void (not a variable type) [Action 1]
def p_void_type(p):
	'void_type : '
	current_program.current_type = "void"

#Adds the function to the FuncDirectory structure [Action 2]
def p_add_module(p):
	'add_module : '
	current_program.scope_l = p[-1]
	add_module_to_directory(current_program)

#Add each parameter one by one as they are analized [Action 3]
def p_add_parameter(p):
	'add_parameter : '
	add_parameter_to_function(current_program, p[-1])

#Generates both the return quad and the GOTO to return to functioncall location [Action 4]
def p_return_quad(p):
	'return_quad : '
	return_from_function(current_program)

#Generates the ENDPROC to represent end of function [Action 5]
def p_endproc_quad(p):
	'endproc_quad : '
	current_program.mem.clear_temporary_memory()
	current_program.quad_number += quad_append(current_program, 
		Quad(current_program.quad_number, "ENDPROC", None, None, None))



#Statement Syntax Diagram Representation
def p_statement(p):
	'''statement : assignment EOS
			| print EOS
			| functioncall EOS
			| condition
			| specialfunction EOS
			| input EOS'''





#This function is used by every one of the following syntax diagram representations
#to evaluate binary operations of logical, relational, multiplication/division, and
#addition/subtraction operations [Action 1]
def evaluate_expression(p):
	current_program.quad_number += evaluate_binary_operation(current_program)





#Compoundexp Syntax Diagram Representation
def p_compoundexp(p):
	'compoundexp : expression eval_logic compoundexp_prime'

def p_compoundexp_prime(p):
	'''compoundexp_prime : AND push_operator compoundexp
			| OR push_operator compoundexp
			| '''

#Checks that the operator is for a logic operation [Action 2]
def p_eval_logic(p):
	'eval_logic :'
	if len(current_program.operator_stack) > 0 and len(current_program.operand_stack) > 1:
		if current_program.operator_stack[-1] == '&&' or current_program.operator_stack[-1] == '||':
			evaluate_expression(p)






#Expression Syntax Diagram Representation
def p_expression(p):
	'expression : exp eval_relational expression_prime'

def p_expression_prime(p):
	'''expression_prime : GREATER push_operator expression
					| LESS push_operator expression
					| EQUAL push_operator expression
					| NOTEQUAL push_operator expression
					| GREATEREQUAL push_operator expression
					| LESSEQUAL push_operator expression
					| '''

#Checks that the operator is for a relational operation [Action 3]
def p_eval_relational(p):
	'eval_relational :'
	if len(current_program.operator_stack) > 0 and len(current_program.operand_stack) > 1:
		if current_program.operator_stack[-1] == '>' or current_program.operator_stack[-1] == '<' or \
		current_program.operator_stack[-1] == '>=' or current_program.operator_stack[-1] == '<=' or \
		current_program.operator_stack[-1] == '==' or current_program.operator_stack[-1] == '!=':
			evaluate_expression(p)





#Exp Syntax Diagram Representation
def p_exp(p):
	'exp : term eval_term exp_prime'

def p_exp_prime(p):
	'''exp_prime : PLUS push_operator exp
					| MINUS push_operator exp
					| '''

#Checks that the operator is for a arithmetical sum/subtraction operation [Action 4]
def p_eval_term(p):
	'eval_term :'
	if len(current_program.operator_stack) > 0 and len(current_program.operand_stack) > 1:
		if current_program.operator_stack[-1] == '+' or current_program.operator_stack[-1] == '-':
			evaluate_expression(p)





#Term Syntax Diagram Representation
def p_term(p):
	'term : factor eval_factor term_prime'

def p_term_prime(p):
	'''term_prime : MULTIPLY push_operator term
			| DIVIDE push_operator term
			| '''

#Checks that the operator is for a arithmetical multiplication/division operation [Action 5]
def p_eval_factor(p):
	'eval_factor :'
	if len(current_program.operator_stack) > 0 and len(current_program.operand_stack) > 1:
		if current_program.operator_stack[-1] == '*' or current_program.operator_stack[-1] == '/':
			evaluate_expression(p)





#Factor Syntax Diagram Representation
def p_factor(p):
	'''factor : LEFTP fake_bottom expression RIGHTP pop_fake_bottom
			| operand
			| PLUS operand
			| MINUS operand'''

#Adds a fake bottom to the operand stack [Action 6]
def p_fake_bottom(p):
	'fake_bottom : '
	current_program.operator_stack.append('[(')

#Pops a fake bottom to the operand stack [Action 7]
def p_pop_fake_bottom(p):
	'pop_fake_bottom : '
	current_program.operator_stack.pop()





#Operand Syntax Diagram Representation
def p_operand(p):
	'''operand : CSTI evaluate_operation_int
			| CSTF evaluate_operation_float
			| CSTC evaluate_operation_char
			| ID push_id operand_prime'''

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

#Pushes an id (address) for a variable into the operand stack [Action 8]
def p_push_id(p):
	'push_id : '
	push_id_to_stack(current_program, p[-1])

#Pushes a constant into the operand stack [Action 8,9,10]
def p_evaluate_operation_int(p):
	'evaluate_operation_int : '
	push_constant_to_stack(current_program, p[-1], 'int')

def p_evaluate_operation_float(p):
	'evaluate_operation_float : '
	push_constant_to_stack(current_program, p[-1], 'float')

def p_evaluate_operation_char(p):
	'evaluate_operation_char : '
	push_constant_to_stack(current_program, p[-1], 'char')





#Assignment Syntax Diagram Representation
def p_assignment(p):
	'assignment : ID push_id assignment_prime EQUALS push_operator expression eval_assignment'

def p_assignment_prime(p):
	'''assignment_prime : 
				   | LEFTB exp RIGHTB assignment_second_prime'''

def p_assignment_second_prime(p):
	'''assignment_second_prime : 
				   | LEFTB exp RIGHTB'''
	current_program.current_dim = 1

#Evaluates assignment [Action 1]
def p_eval_assignment(p):
	'eval_assignment : '
	evaluate_assignment(current_program)
	current_program.quad_number += 1





#Condition Syntax Diagram Representation
def p_condition(p):
	'''condition : WHILE save_jump LEFTP compoundexp RIGHTP gotof_quad LEFTBRACE body RIGHTBRACE goto_while_fill
				   | DO save_jump LEFTBRACE body RIGHTBRACE WHILE LEFTP compoundexp RIGHTP gotov_quad
				   | IF condition_prime'''

def p_condition_prime(p):
	'condition_prime : LEFTP compoundexp RIGHTP gotof_quad condition_second_prime'

def p_condition_second_prime(p):
	'''condition_second_prime : statement condition_third_prime
					| LEFTBRACE body RIGHTBRACE condition_third_prime'''

def p_condition_third_prime(p):
	'''condition_third_prime : goto_if_fill ELSEIF condition_prime
					| ELSE goto_else condition_fourth_prime
					| goto_if_fill'''

def p_condition_fourth_prime(p):
	'''condition_fourth_prime : statement goto_if_fill
					| LEFTBRACE body RIGHTBRACE goto_if_fill'''

def p_save_jump(p):
	'save_jump :'
	current_program.jump_stack.append(current_program.quad_number)

def p_gotof_quad(p):
	'gotof_quad :'
	exp_type = current_program.type_stack.pop()
	if exp_type == 'bool':
		result = current_program.operand_stack.pop()
		current_program.quad_number += quad_append(current_program, 
			Quad(current_program.quad_number, 'GOTOF', result, None, None))
		current_program.jump_stack.append(current_program.quad_number - 2)
	else:
		print("Type mismatch at condition.")

def p_goto_else(p):
	'goto_else : '
	end = current_program.jump_stack.pop();
	current_program.quad_number += quad_append(current_program,
	 Quad(current_program.quad_number, "GOTO", None, None, None))
	quad = current_program.quad_list[end]
	end = current_program.jump_stack.append(current_program.quad_number-2);
	quad.set_quad_goto(current_program.quad_number)

def p_gotov_quad(p):
	'gotov_quad : '
	exp_type = current_program.type_stack.pop()
	if exp_type == 'bool':
		result = current_program.operand_stack.pop()
		quad_hop = current_program.jump_stack.pop()
		current_program.quad_number += quad_append(current_program, 
			Quad(current_program.quad_number, 'GOTOV', result, None, quad_hop))
	else:
		print("Type mismatch at condition.")

def p_goto_if_fill(p):
	'goto_if_fill :'
	end = current_program.jump_stack.pop();
	quad = current_program.quad_list[end]
	quad.set_quad_goto(current_program.quad_number)

def p_goto_while_fill(p):
	'goto_while_fill :'
	end = current_program.jump_stack.pop();
	ret = current_program.jump_stack.pop();
	current_program.quad_number += quad_append(current_program, Quad(current_program.quad_number, "GOTO", None, None, ret))
	quad = current_program.quad_list[end]
	quad.set_quad_goto(current_program.quad_number)





#Functioncall Syntax Diagram Representation
def p_functioncall(p):
	'functioncall : ID verify_function LEFTP fake_bottom exp verify_parameter functioncall_prime'

def p_functioncall_prime(p):
	'''functioncall_prime : SEPARATOR exp verify_parameter functioncall_prime
					| verify_param_count RIGHTP pop_fake_bottom store_memory_data go_sub_quad'''

def p_verify_function(p):
	'verify_function : '
	current_program.current_func_id = p[-1]
	current_program.quad_number += era_quad(current_program, p[-1])
	current_program.param_evaluation_counter = 0

def p_verify_parameter(p):
	'verify_parameter : '
	current_program.quad_number += param_quad(current_program)
	current_program.param_evaluation_counter += 1

def p_verify_param_count(p):
	'verify_param_count : '
	current_function = current_program.func_directory.get_function(current_program.current_func_id)
	if current_program.param_evaluation_counter != current_function['parameters']['parameter_counter']:
		print("Error: Expected " + str(current_function['parameters']['parameter_counter'])
			+ " arguments for call to function " + p[-6] + ".")

def p_store_memory_data(p):
	'store_memory_data : '
	current_program.jump_stack.append(current_program.quad_number)

def p_go_sub_quad(p):
	'go_sub_quad : '
	target = current_program.current_func_id
	current_program.quad_number += gosub_quad(current_program, target)


def p_push_operator(p):
	'push_operator : '
	current_program.operator_stack.append(p[-1])





#Print Syntax Diagram Representation
def p_print(p):
	'print : PRINT LEFTP expression print_quad print_prime'

def p_print_prime(p):
	'''print_prime : SEPARATOR expression print_quad print_prime
					| RIGHTP'''

def p_print_quad(p):
	'print_quad : '
	print_content = current_program.operand_stack.pop()
	current_program.quad_number += quad_append(current_program, 
		Quad(current_program.quad_number, 'PRINT', print_content, None, None))





#SpecialFunction Syntax Diagram Representation
def p_specialfunction(p):
	'specialfunction : JEDO POINT specialfunction_prime'

def p_specialfunction_prime(p):
	'''specialfunction_prime : CIRCLE LEFTP exp RIGHTP one_argument_quad
			| SQUARE LEFTP exp RIGHTP one_argument_quad
			| RECTANGLE LEFTP exp SEPARATOR exp RIGHTP two_argument_quad
			| TRIANGLE LEFTP exp RIGHTP one_argument_quad
			| FORWARD LEFTP exp RIGHTP one_argument_quad
			| BACK LEFTP exp RIGHTP one_argument_quad
			| TURNRIGHT LEFTP exp RIGHTP one_argument_quad
			| TURNLEFT LEFTP exp RIGHTP one_argument_quad
			| COLOR LEFTP exp SEPARATOR exp SEPARATOR exp RIGHTP three_argument_quad
			| THICKNESS LEFTP exp RIGHTP one_argument_quad
			| STARTPEN LEFTP RIGHTP no_argument_quad
			| STOPPEN LEFTP RIGHTP no_argument_quad
			| STARTFILL LEFTP RIGHTP no_argument_quad
			| FILLSHAPE LEFTP exp SEPARATOR exp SEPARATOR exp RIGHTP three_argument_quad
			| STOPFILL LEFTP RIGHTP no_argument_quad
			| RESTART LEFTP RIGHTP no_argument_quad
			| '''

def p_no_argument_quad(p):
	'no_argument_quad :'
	special_function = p[-3]
	no_argument_special_function(current_program, special_function)

def p_one_argument_quad(p):
	'one_argument_quad :'
	special_function = p[-4]
	one_argument_special_function(current_program, special_function)

def p_two_argument_quad(p):
	'two_argument_quad :'
	special_function = p[-6]
	two_argument_special_function(current_program, special_function)

def p_three_argument_quad(p):
	'three_argument_quad :'
	special_function = p[-8]
	three_argument_special_function(current_program, special_function)





def p_input(p):
	'input : READINPUT LEFTP ID input_quad RIGHTP'

def p_input_quad(p):
	'input_quad : '
	identifier = current_program.func_directory.get_function_variable(current_program.scope_l, p[-1])
	if identifier is None:
		identifier = current_program.func_directory.get_function_variable(current_program.scope_g, p[-1])
		if identifier is not None:
			current_program.quad_number += quad_append(current_program, 
				Quad(current_program.quad_number, "READINPUT", identifier['type'], None, identifier['address']))
		else:
			print("The variable " + p[-1] + " has not been declared.")
			sys.exit()
	else:
		current_program.quad_number = quad_append(current_program, 
			Quad(current_program.quad_number, "READINPUT", identifier['type'], None, identifier['address']))






#Executes parser
import ply.yacc as yacc
import pprint
parser = yacc.yacc()

pp = pprint.PrettyPrinter(indent=4)
with open('test.txt','r') as f:
	input = f.read()
pp.pprint(parser.parse(input))
indexval = 0
for i in range(len(current_program.quad_list)):     
    print(current_program.quad_list[indexval])
    indexval += 1

current_program.func_directory.print_directory()
