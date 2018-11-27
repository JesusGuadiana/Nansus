# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  twoArgumentSpecialFunctionIntString.py
#  Last edit: 20/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from functions.quadGenerator import quad_append
from structures.quad import Quad
import sys

def two_argument_string_special_function(current_program, element, string):
	current_type = current_program.type_stack.pop()
	#Only one of the variables is stored, the string is just passing by.
	if current_type == "int":
		operand = current_program.operand_stack.pop()
		current_program.quad_number += quad_append(current_program,
			   Quad(current_program.quad_number, element, operand, string, None))
	else:
		print("Special Functions parameter type mismatch.")
		sys.exit()
