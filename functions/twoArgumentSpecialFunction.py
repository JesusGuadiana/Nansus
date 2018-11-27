# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  twoArgumentSpecialFunction.py
#  Last edit: 20/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from functions.quadGenerator import quad_append
from structures.quad import Quad
import sys

def two_argument_special_function(current_program, element):
	current_type = current_program.type_stack.pop()
	current_type2 = current_program.type_stack.pop()
	#Since we are verifying two int exps, two verificaitions are in check
	if current_type == "int":
		if current_type2 == "int":
			operand = current_program.operand_stack.pop()
			operand2 = current_program.operand_stack.pop()
			current_program.quad_number += quad_append(current_program,
				Quad(current_program.quad_number, element, operand, operand2, None))
		else:
			print("Special functions paramter type mismatch.")
			sys.exit()
