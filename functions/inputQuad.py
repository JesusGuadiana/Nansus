# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  inputQuad.py
#  Last edit: 21/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from functions.evaluateExpression import evaluate_binary_operation
from functions.quadGenerator import quad_append
from structures.quad import Quad
import sys
def input_quad_function(current_program, element):
	#Although we do it often, it's important to note that these two functions will usually act as a way
	#to check both local and global context
	identifier = current_program.func_directory.get_function_variable(current_program.scope_l, element)
	if identifier is None:
		identifier = current_program.func_directory.get_function_variable(current_program.scope_g, element)
		if identifier is not None:
			#Type is a literal value in this quadruple
			current_program.quad_number += quad_append(current_program,
				Quad(current_program.quad_number, "READINPUT", identifier['type'], None, identifier['address']))
		else:
			print("The variable " + element + " has not been declared.")
			sys.exit()
	else:
		current_program.quad_number += quad_append(current_program,
			Quad(current_program.quad_number, "READINPUT", identifier['type'], None, identifier['address']))