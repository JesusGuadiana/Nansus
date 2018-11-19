# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  oneArgumentSpecialFunction.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
from functions.quadGenerator import quad_append
from structures.quad import Quad

def one_argument_special_function(current_program, element):
	operand = current_program.operand_stack.pop()
	current_program.quad_number += quad_append(current_program, 
		Quad(current_program.quad_number, element, operand, None, None))