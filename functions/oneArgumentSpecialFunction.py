# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  oneArgumentSpecialFunction.py
#  Last edit: 20/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from functions.quadGenerator import quad_append
from structures.quad import Quad
import sys

def one_argument_special_function(current_program, element):
	#This will pop the expression for the argument and verify it is an int
	current_type = current_program.type_stack.pop()
	if current_type == "int":
		operand = current_program.operand_stack.pop()
		current_program.quad_number += quad_append(current_program,
			Quad(current_program.quad_number, element, operand, None, None))
	else:
		print("Special functions parameter type mismatch.")
		sys.exit()
