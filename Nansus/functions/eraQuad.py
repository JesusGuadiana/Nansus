# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  eraQuad.py
#  Last edit: 17/11/2018
# -----------------------------------------------------------------------------
from functions.quadGenerator import quad_append
from structures.quad import Quad

def era_quad(current_program, element):
	if current_program.func_directory.get_function(element) is not None:
		current_program.quad_number += quad_append(current_program, 
			Quad(current_program.quad_number, 'ERA', element, None, None))
		function_parameters = current_program.func_directory.get_function_parameters(element)
		current_program.temporary_arg_types = list(function_parameters['parameter_types'])
		return 1
	else:
		print("Function " + element + " is not defined.")
		return 0