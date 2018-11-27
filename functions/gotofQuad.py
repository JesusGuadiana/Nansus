# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  gotofQuad.py
#  Last edit: 21/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from functions.evaluateExpression import evaluate_binary_operation
from functions.quadGenerator import quad_append
from structures.quad import Quad
import sys

def gotof_quad_function(current_program):
	exp_type = current_program.type_stack.pop()
	#It is very important that this verification is here, otherwise it would just be a goto
	if exp_type == 'bool':
		result = current_program.operand_stack.pop()
		current_program.quad_number += quad_append(current_program,
			Quad(current_program.quad_number, 'GOTOF', result, None, None))
		current_program.jump_stack.append(current_program.quad_number - 2)
	else:
		print("Type mismatch at condition.")
		sys.exit()