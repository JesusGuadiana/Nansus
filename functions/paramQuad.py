# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  paramQuad.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from structures.quad import Quad
from functions.quadGenerator import quad_append
import sys

def param_quad(current_program):
	if current_program.temporary_arg_types:
		arg_value = current_program.operand_stack.pop()
		arg_type = current_program.type_stack.pop()
		param_type = current_program.temporary_arg_types.pop()
		if arg_type == param_type:
			#Parameters store the position of their variables
			current_program.quad_number += quad_append(current_program, 
			Quad(current_program.quad_number, 'PARAMETER', arg_value, None, None))
			return 1
		else:
			sys.exit()
	else:
		print(current_program.temporary_arg_types)
		sys.exit()