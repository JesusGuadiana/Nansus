# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  nansus.py
#  Last edit: 24/11/2018
# -----------------------------------------------------------------------------
#Python Lexer & Yacc
from ply import *

#Main Program Structure Import
from currentProgram import CurrentProgram

#Import Virtual Machine
from vm import Machine

#Structure imports
from structures.funcDirectory import FuncDirectory
from structures.quad import Quad
from structures.semCube import SemanticCube

#Function imports
from functions.addModules import add_module_to_directory
from functions.addParameter import add_parameter_to_function
from functions.addVariable import add_variable_to_directory
from functions.addVectorOrMatrix import add_vector_or_matrix
from functions.eraQuad import era_quad
from functions.evaluateAssign import evaluate_assignment
from functions.evaluateExpression import evaluate_binary_operation
from functions.evaluateOperation import evaluate_operation
from functions.functionReturn import return_from_function
from functions.gosubQuad import gosub_quad
from functions.gotoElse import goto_else_function
from functions.gotofQuad import gotof_quad_function
from functions.gotovQuad import gotov_quad_function
from functions.inputQuad import input_quad_function
from functions.noArgumentSpecialFunction import no_argument_special_function
from functions.oneArgumentSpecialFunction import one_argument_special_function
from functions.paramQuad import param_quad
from functions.printToOutputFile import print_to_output_file
from functions.pushConstant import push_constant_to_stack
from functions.pushId import push_id_to_stack
from functions.quadGenerator import quad_append
from functions.quadVer import quad_ver_function, quad_ver_two_function
from functions.twoArgumentSpecialFunction import two_argument_special_function
from functions.twoArgumentSpecialFunctionIntString import two_argument_string_special_function

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
#Receive Program id and place a ;
def p_program(p):
	'program : PRGM ID main_quad add_program_function EOS program_prime'

#Cycle through global variables and modules declaration (order doesn't matter)
def p_program_prime(p):
	'''program_prime : vars program_prime
					| modules program_prime
					| program_second_prime'''

#Declares the main function space (change local context to main in fill_main) and opens the body
def p_program_second_prime(p):
	'program_second_prime : MAIN fill_main LEFTBRACE program_third_prime'

#Cycle through variable declaration (only allowed at the start) and then proceed to cycle through
#statements (body)
def p_program_third_prime(p):
	'''program_third_prime : vars program_third_prime
							| body RIGHTBRACE EOS'''


#Calls function to create the default GOTO MAIN quadruple
def p_main_quad(p):
	'main_quad : '
	current_program.quad_number += quad_append(current_program, Quad(current_program.quad_number,
	 "GOTO", "MAIN", None, None))


#Calls function to add the program function to the function directory
def p_add_program_function(p):
	'add_program_function : '
	current_program.scope_g = p[-2] #Both of these functions are at the moment equal to the global context
	current_program.scope_l = p[-2] #whose name is defined by the program name that comes in the test file
	current_program.func_directory.new_function(current_program.scope_g, 'void')


#Completes the main quad with the quadruple to which it has to go to at the start of program
#and then proceeds to make the main context the current local scope, as well as adding it to
#the function directory 
def p_fill_main(p):
	'fill_main : '
	quad = current_program.quad_list[0]
	quad.set_quad_goto(current_program.quad_number)
	current_program.scope_l = p[-1]
	current_program.func_directory.new_function(current_program.scope_l, 'void')





#Vars Syntax Diagram Grammar Representation
#Redirects to type, and then continues with variable declaration
def p_vars(p):
	'vars : type vars_prime vars_third_prime '

#Reads the id, saves it to a variable within the CurrentProgram structure for use
def p_vars_prime(p):
	'vars_prime : ID save_id vars_second_prime'

#After entering here, if it finds square brackets it will change the dimension flag to indicate that
#it is currently handling an array
def p_vars_second_prime(p):
	'''vars_second_prime : change_dimension LEFTB exp RIGHTB first_dimension vars_fifth_prime
						| '''

#Here it will look to see if more than one variable was declared, and cycle through the previous
#instructions, otherwise it will store the variable and proceed
def p_vars_third_prime(p):
	'''vars_third_prime : SEPARATOR store_variable vars_prime vars_third_prime
				   | store_variable vars_fourth_prime'''

#Ends the declaration of variables
def p_vars_fourth_prime(p):
	'vars_fourth_prime : EOS'

def p_vars_fifth_prime(p):
	'''vars_fifth_prime : LEFTB exp RIGHTB second_dimension allocate_sequential_memory set_internal_dimension_one set_internal_dimension_two
						| allocate_sequential_memory set_internal_dimension_one'''



#Save the id name in the global structure for easy usage 
def p_save_id(p):
	'save_id : '
	current_program.current_id = p[-1]

#Change flag for dimensioned variable within the main program structure
def p_change_dimension(p):
	'change_dimension : '
	current_program.vec_mat_variable_flag = True

#Adds the variable to the funcDirectory in the current function
def p_store_variable(p):
	'store_variable : '
	if not current_program.vec_mat_variable_flag:
		add_variable_to_directory(current_program)
	current_program.vec_mat_variable_flag = False

#Handles information to store the the indexed dimension of the array
def p_first_dimension(p):
	'first_dimension : '
	exp_type = current_program.type_stack.pop()
	if exp_type == 'int':
		result = current_program.operand_stack.pop()
		current_program.vec_mat_first_dimension = result
	else:
		print("Type mismatch at index.")
		sys.exit()

def p_second_dimension(p):
	'second_dimension : '
	exp_type = current_program.type_stack.pop()
	if exp_type == 'int':
		result = current_program.operand_stack.pop()
		current_program.vec_mat_second_dimension = result
	else:
		print("Type mismatch at index.")
		sys.exit()

#Creates memory location for the array and assigns it the value of its indexed dimension
def p_set_internal_dimension_one(p):
	'set_internal_dimension_one : '
	current_program.func_directory.set_local_variable_dimension_one(
			current_program.scope_l, current_program.current_type, current_program.current_id,
			current_program.mem.get_content(current_program.vec_mat_first_dimension))

def p_set_internal_dimension_two(p):
	'set_internal_dimension_two : '
	
	current_program.func_directory.set_local_variable_dimension_two(
			current_program.scope_l, current_program.current_type, current_program.current_id,
			current_program.mem.get_content(current_program.vec_mat_second_dimension))

def p_allocate_sequential_memory(p):
	'allocate_sequential_memory :'
	base_address = add_vector_or_matrix(current_program)


#Type Syntax Diagram Representation
#Three types handled: int, float, char
def p_type(p):
	'''type : TYPEINT
			| TYPEFLOAT
			| TYPECHAR'''

	#Changes the current type for variable analysis
	current_program.current_type = p[1]






#Body Syntax Diagram Representation
#This is a representation of the content within function/main to cycle through statements
def p_body(p):
	'body : statement body_prime'

def p_body_prime(p):
	'''body_prime : body
				   | '''






#Module Syntax Diagram Representation
#Names function and provides id, following into parameter declaration
def p_modules(p):
	'modules : FUNCTION modules_prime ID add_module LEFTP modules_second_prime'

#Assigns either a type or void type (important to avoid void variables) to the function
def p_modules_prime(p):
	'''modules_prime : type
				   | NOTYPE void_type'''

#States the type for the first parameter and provides its id, which is then added
def p_modules_second_prime(p):
	'modules_second_prime : type ID add_parameter modules_third_prime'

#Cycles through the parameter declaration and ends with the right parentheses
def p_modules_third_prime(p):
	'''modules_third_prime : SEPARATOR modules_second_prime
				   | RIGHTP LEFTBRACE modules_fourth_prime'''

#Represents the body, restricts variable declaration to beginning of the body
def p_modules_fourth_prime(p):
	'''modules_fourth_prime : vars modules_fourth_prime
							| body modules_fifth_prime'''

#Generates return or procedes to close a return-less function
def p_modules_fifth_prime(p):
	'''modules_fifth_prime : RETURN exp return_quad EOS RIGHTBRACE endproc_quad print_me
							| RIGHTBRACE endproc_quad print_me'''

def p_print_me(p):
	'print_me :'


#Sets the current type to void (not a variable type)
def p_void_type(p):
	'void_type : '
	current_program.current_type = "void"

#Adds the function to the FuncDirectory structure
def p_add_module(p):
	'add_module : '
	current_program.scope_l = p[-1]
	add_module_to_directory(current_program)

#Add each parameter one by one as they are analized 
def p_add_parameter(p):
	'add_parameter : '
	add_parameter_to_function(current_program, p[-1])

#Generates both the return quad and the GOTO to return to functioncall location 
def p_return_quad(p):
	'return_quad : '
	return_from_function(current_program)

#Generates the ENDPROC to represent end of function
def p_endproc_quad(p):
	'endproc_quad : '
	current_program.quad_number += quad_append(current_program,
		Quad(current_program.quad_number, "ENDPROC", None, None, None))



#Statement Syntax Diagram Representation
#Goes to any of the six type of elements (conditions do not end with ";")
def p_statement(p):
	'''statement : assignment EOS
			| print EOS
			| functioncall EOS
			| condition
			| specialfunction EOS
			| input EOS'''





#This function is used by every one of the following syntax diagram representations
#to evaluate binary operations of logical, relational, multiplication/division, and
#addition/subtraction operations
def evaluate_expression(p):
	current_program.quad_number += evaluate_binary_operation(current_program)





#Compoundexp Syntax Diagram Representation
#Solves binary expressions at logical level (&& and ||)
def p_compoundexp(p):
	'compoundexp : expression eval_logic compoundexp_prime'

def p_compoundexp_prime(p):
	'''compoundexp_prime : AND push_operator compoundexp
			| OR push_operator compoundexp
			| '''

#Checks that the operator is for a logic operation
def p_eval_logic(p):
	'eval_logic :'
	if len(current_program.operator_stack) > 0 and len(current_program.operand_stack) > 1:
		if current_program.operator_stack[-1] == '&&' or current_program.operator_stack[-1] == '||':
			evaluate_expression(p)






#Expression Syntax Diagram Representation
#Solves binary expressions at relational level (>, <, ==, etc.)
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

#Checks that the operator is for a relational operation 
def p_eval_relational(p):
	'eval_relational :'
	if len(current_program.operator_stack) > 0 and len(current_program.operand_stack) > 1:
		if current_program.operator_stack[-1] == '>' or current_program.operator_stack[-1] == '<' or \
		current_program.operator_stack[-1] == '>=' or current_program.operator_stack[-1] == '<=' or \
		current_program.operator_stack[-1] == '==' or current_program.operator_stack[-1] == '!=':
			evaluate_expression(p)





#Exp Syntax Diagram Representation
#Solves binary expressions at term level (+ and -)
def p_exp(p):
	'exp : term eval_term exp_prime'

def p_exp_prime(p):
	'''exp_prime : PLUS push_operator exp
					| MINUS push_operator exp
					| '''

#Checks that the operator is for a arithmetical sum/subtraction operation
def p_eval_term(p):
	'eval_term :'
	if len(current_program.operator_stack) > 0 and len(current_program.operand_stack) > 1:
		if current_program.operator_stack[-1] == '+' or current_program.operator_stack[-1] == '-':
			evaluate_expression(p)





#Term Syntax Diagram Representation
#Solves binary expressions at factor level (*) and /)
def p_term(p):
	'term : factor eval_factor term_prime'

def p_term_prime(p):
	'''term_prime : MULTIPLY push_operator term
			| DIVIDE push_operator term
			| '''

#Checks that the operator is for a arithmetical multiplication/division operation
def p_eval_factor(p):
	'eval_factor :'
	if len(current_program.operator_stack) > 0 and len(current_program.operand_stack) > 1:
		if current_program.operator_stack[-1] == '*' or current_program.operator_stack[-1] == '/':
			evaluate_expression(p)





#Factor Syntax Diagram Representation
#Manages content at the lowest level
def p_factor(p):
	'''factor : LEFTP fake_bottom expression RIGHTP pop_fake_bottom
			| operand '''

#Adds a fake bottom to the operand stack 
def p_fake_bottom(p):
	'fake_bottom : '
	current_program.operator_stack.append('[(')

#Pops a fake bottom to the operand stack 
def p_pop_fake_bottom(p):
	'pop_fake_bottom : '
	current_program.operator_stack.pop()





#Operand Syntax Diagram Representation
#Inserts values for expression into operand stack
def p_operand(p):
	'''operand : CSTI evaluate_operation_int
			| CSTF evaluate_operation_float
			| CSTC evaluate_operation_char
			| ID push_id save_id_operand operand_prime
			| FUNCTION functioncall'''

def p_save_id_operand(p):
	'save_id_operand :'
	current_program.current_id = p[-2]

def p_save_id_array(p):
	'save_id_array :'
	current_program.current_array_id = current_program.current_id


def p_operand_prime(p):
	'''operand_prime : save_id_array LEFTB fake_bottom exp RIGHTB pop_fake_bottom operand_second_prime
			| '''

def p_operand_second_prime(p):
	'''operand_second_prime : LEFTB fake_bottom exp RIGHTB pop_fake_bottom quad_ver_two
			| quad_ver_one'''

#Pushes an id (address) for a variable into the operand stack 
def p_push_id(p):
	'push_id : '
	push_id_to_stack(current_program, p[-1])

#Pushes a constant into the operand stack (by type)
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
	'assignment : ID push_id save_assignment_id assignment_second_prime EQUALS push_operator assignment_prime'

def p_assignment_prime(p):
    '''assignment_prime : exp eval_assignment'''


def p_assignment_second_prime(p):
	'''assignment_second_prime :
				   | save_id_array LEFTB fake_bottom exp RIGHTB pop_fake_bottom assignment_third_prime'''

def p_assignment_third_prime(p):
	'''assignment_third_prime : LEFTB fake_bottom exp RIGHTB pop_fake_bottom quad_ver_two
							| quad_ver_one'''

#Generates VER quadruple for index management in arrays
def p_quad_ver_one(p):
	'quad_ver_one :'
	quad_ver_function(current_program)

def p_quad_ver_two(p):
	'quad_ver_two :'
	quad_ver_two_function(current_program)

#Evaluates assignment
def p_eval_assignment(p):
	'eval_assignment : '
	evaluate_assignment(current_program)
	current_program.quad_number += 1

#Useful to find the data when using it for comparisons
def p_save_assignment_id(p):
	'save_assignment_id : '
	current_program.current_id = p[-2]





#Condition Syntax Diagram Representation
#Full declaration of both while and do, start of if
def p_condition(p):
	'''condition : WHILE save_jump LEFTP compoundexp RIGHTP gotof_quad LEFTBRACE body RIGHTBRACE goto_while_fill
				   | DO save_jump LEFTBRACE body RIGHTBRACE WHILE LEFTP compoundexp RIGHTP gotov_quad
				   | IF condition_prime'''

#Open if parentheses
def p_condition_prime(p):
	'condition_prime : LEFTP compoundexp RIGHTP gotof_quad condition_second_prime' #Here the gotof is generated

#The content of the if can either be a single statement or a braced series of statements
def p_condition_second_prime(p):
	'''condition_second_prime : statement condition_third_prime
					| LEFTBRACE body RIGHTBRACE condition_third_prime'''

#Fills the goto values since it finishes the section, and gives the option to proceed to an elseif or else
def p_condition_third_prime(p):
	'''condition_third_prime : goto_if_fill ELSEIF condition_prime
					| ELSE goto_else condition_fourth_prime
					| goto_if_fill'''

#A single statement or a group of braced statetements followed by the action of filling in the gaps within the goto
def p_condition_fourth_prime(p):
	'''condition_fourth_prime : statement goto_if_fill
					| LEFTBRACE body RIGHTBRACE goto_if_fill'''

#Adds content to the jump stack for filling GOTO quads
def p_save_jump(p):
	'save_jump :'
	current_program.jump_stack.append(current_program.quad_number)

#Generates the GOTOF quad for while, if, and elseif
def p_gotof_quad(p):
	'gotof_quad :'
	gotof_quad_function(current_program)

#Generates the GOTO whenever an else appears or at the end of while
def p_goto_else(p):
	'goto_else : '
	goto_else_function(current_program)

#Generates the GOTOV for the do while condition
def p_gotov_quad(p):
	'gotov_quad : '
	gotov_quad_function(current_program)

#Fills the jump value of the if version of the goto
def p_goto_if_fill(p):
	'goto_if_fill :'
	end = current_program.jump_stack.pop();
	quad = current_program.quad_list[end]
	quad.set_quad_goto(current_program.quad_number)

#Fills the jump value of the while version of the goto
def p_goto_while_fill(p):
	'goto_while_fill :'
	end = current_program.jump_stack.pop();
	ret = current_program.jump_stack.pop();
	current_program.quad_number += quad_append(current_program, Quad(current_program.quad_number, "GOTO", None, None, ret))
	quad = current_program.quad_list[end]
	quad.set_quad_goto(current_program.quad_number)





#Functioncall Syntax Diagram Representation
#The function call declares the id and opens the parenthesis, every parameter is verified
def p_functioncall(p):
	'functioncall : ID verify_function LEFTP fake_bottom exp verify_parameter functioncall_prime'

#Keeps verifying parameters, ends when it finds the end of the fake bottom and proceeds to jump to function
def p_functioncall_prime(p):
	'''functioncall_prime : SEPARATOR exp verify_parameter functioncall_prime
					| verify_param_count RIGHTP pop_fake_bottom go_sub_quad'''

#Generates the ERA quad, which will have information for the Activation Register at the time of execution
def p_verify_function(p):
	'verify_function : '
	current_program.current_func_id = p[-1]
	current_program.quad_number += era_quad(current_program, p[-1])
	current_program.param_evaluation_counter = 0

#One by one, verifies that each paramter is satisfactory to the signature of the function
def p_verify_parameter(p):
	'verify_parameter : '
	current_program.quad_number += param_quad(current_program)
	current_program.param_evaluation_counter += 1

#One the params are all received, this command checks to see that the number of parameters matches the signature
def p_verify_param_count(p):
	'verify_param_count : '
	current_function = current_program.func_directory.get_function(current_program.current_func_id)
	if current_program.param_evaluation_counter != current_function['parameters']['parameter_counter']:
		print("Error: Expected " + str(current_function['parameters']['parameter_counter'])
			+ " arguments for call to function " + p[-6] + ".")

#Generates the GOsub quadruple and adds it to the list
def p_go_sub_quad(p):
	'go_sub_quad : '
	target = current_program.current_func_id
	current_program.quad_number += gosub_quad(current_program, target)


#Pushes an operator into the stack
def p_push_operator(p):
	'push_operator : '
	current_program.operator_stack.append(p[-1])





#Print Syntax Diagram Representation
#Declares print and opens a fake bottom
def p_print(p):
	'print : PRINT LEFTP fake_bottom print_prime'

#Followed by an expression of any type of the three accepted variables, as well as literal strings
def p_print_prime(p):
	'''print_prime : expression print_quad print_second_prime
					| CSTS print_string_quad print_second_prime'''

#Separates the outputs the user wishes and treats every one indiviudually
def p_print_second_prime(p):
	'''print_second_prime : SEPARATOR expression print_quad print_second_prime
					| RIGHTP pop_fake_bottom'''

#Generates the PRINT quad
def p_print_quad(p):
	'print_quad : '
	print_content = current_program.operand_stack.pop()
	print_type = current_program.type_stack.pop()
	current_program.quad_number += quad_append(current_program,
		Quad(current_program.quad_number, 'PRINT', print_content, None, None))

#Generates the specific type of PRINT quad that uses a string (since it is uniquely stored)
def p_print_string_quad(p):
	'print_string_quad : '
	temporary_string = current_program.mem.temporary_memory_assign('string', p[-1])
	current_program.quad_number += quad_append(current_program,
		Quad(current_program.quad_number, 'PRINT', temporary_string, None, None))



#SpecialFunction Syntax Diagram Representation
#Jedo.specialfunction
def p_specialfunction(p):
	'specialfunction : JEDO POINT specialfunction_prime'

#Every single function that jedo can execute (based on turtle)
def p_specialfunction_prime(p):
	'''specialfunction_prime : CIRCLE LEFTP exp RIGHTP one_argument_quad
			| SQUARE LEFTP exp RIGHTP one_argument_quad
			| RECTANGLE LEFTP exp SEPARATOR exp RIGHTP two_argument_quad
			| DRAWDOT LEFTP exp SEPARATOR CSTS RIGHTP two_argument_string_quad
			| ARCH LEFTP exp SEPARATOR CSTS RIGHTP two_argument_string_quad
			| TRIANGLE LEFTP exp RIGHTP one_argument_quad
			| FORWARD LEFTP exp RIGHTP one_argument_quad
			| BACK LEFTP exp RIGHTP one_argument_quad
			| TURNRIGHT LEFTP exp RIGHTP one_argument_quad
			| TURNLEFT LEFTP exp RIGHTP one_argument_quad
			| COLOR LEFTP CSTS RIGHTP special_string_quad
			| THICKNESS LEFTP exp RIGHTP one_argument_quad
			| STARTPEN LEFTP RIGHTP no_argument_quad
			| CREATE LEFTP RIGHTP no_argument_quad
			| STOPPEN LEFTP RIGHTP no_argument_quad
			| STARTFILL LEFTP RIGHTP no_argument_quad
			| FILLSHAPE LEFTP CSTS RIGHTP special_string_quad
			| STOPFILL LEFTP RIGHTP no_argument_quad
			| RESTART LEFTP RIGHTP no_argument_quad
			| '''

#For those functions that don't requiere parameters
def p_no_argument_quad(p):
	'no_argument_quad :'
	special_function = p[-3]
	no_argument_special_function(current_program, special_function)

#For those functions that require one int argument
def p_one_argument_quad(p):
	'one_argument_quad :'
	special_function = p[-4]
	one_argument_special_function(current_program, special_function)

#For those functions that require two int arguments
def p_two_argument_quad(p):
	'two_argument_quad :'
	special_function = p[-6]
	two_argument_special_function(current_program, special_function)

#For those functions that require one int argument and one string argument
def p_two_argument_string_quad(p):
	'two_argument_string_quad :'
	special_function = p[-6]
	two_argument_string_special_function(current_program, special_function, p[-2])

#For those functions that require one string argument
def p_special_string_quad(p):
	'special_string_quad :'
	temporary_string = current_program.mem.temporary_memory_assign('string', p[-2])
	current_program.quad_number += quad_append(current_program,
		Quad(current_program.quad_number, p[-4], temporary_string, None, None))




#Input Syntax Diagram Representation
#ReadInput followed by the ID where the input will be stored and closed rightaway (no multi-input)
def p_input(p):
	'input : READINPUT LEFTP ID input_quad RIGHTP'

#Generates the READINPUT quadruple
def p_input_quad(p):
	'input_quad : '
	input_quad_function(current_program, p[-1])






#Executes parser
import ply.yacc as yacc
import pprint
parser = yacc.yacc()

#Pretty Printer to make the format more pleasant

pp = pprint.PrettyPrinter(indent=4)
with open(lex.filename,'r') as f:
	input = f.read()
pp.pprint(parser.parse(input))

print_to_output_file("\nINTERMEDIATE CODE:\n")

#Prints intermediate code
index = 0
for i in range(len(current_program.quad_list)):
	print_to_output_file(current_program.quad_list[index])
	index += 1

print_to_output_file("\nFUNCTION DIRECTORY:")

current_program.func_directory.print_directory()

#Executres the virtual machine with copies of the memory, function directory and list of quadruples
vm = Machine(current_program.quad_list, current_program.mem, current_program.func_directory)

vm.run_machine();
