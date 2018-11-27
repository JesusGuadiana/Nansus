# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  eraQuad.py
#  Last edit: 24/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from functions.quadGenerator import quad_append
from structures.quad import Quad
import sys


def era_quad(current_program, element):

	if current_program.func_directory.get_function(element) is not None:
		return_address = current_program.func_directory.get_return_address(element)
		function_type = current_program.func_directory.get_function_type(element)
		current_program.operand_stack.append(return_address) #These two lines were not in the first version
		current_program.type_stack.append(function_type)# They insert the return line into the stack
		current_program.quad_number += quad_append(current_program, 
			Quad(current_program.quad_number, 'ERA', element, None, None))
		function_parameters = current_program.func_directory.get_function_parameters(element)
		#This will help us verify that the sent types are of the correct type
		current_program.temporary_arg_types = list(function_parameters['parameter_types'])
		return 1
	else:
		print("Function " + element + " is not defined.")
		sys.exit()