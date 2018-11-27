# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  evaluateAssign.py
#  Last edit: 21/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from structures.quad import Quad
from functions.printToOutputFile import print_to_output_file
import sys

def evaluate_assignment(current_program):
	#Evaluates the assignment
	operator = current_program.operator_stack.pop()
	if operator == '=':
		right_operand = current_program.operand_stack.pop()
		right_type = current_program.type_stack.pop()
		left_operand = current_program.operand_stack.pop()
		left_type = current_program.type_stack.pop()
		result_type = current_program.sem_cube.get_type(left_type, right_type, operator)
		if result_type != 'error':
			#From this format, the value stored is the right_operand and the place it is stored is the left_operand
			quad = Quad(current_program.quad_number, operator, right_operand, None, left_operand)
			current_program.quad_list.append(quad)
		else:
			print('Operation Type Mismatch.')
			sys.exit()