# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  evaluateExpression.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
from structures.quad import Quad
from structures.semCube import SemanticCube
from functions.quadGenerator import quad_append
import sys

def evaluate_binary_operation(current_program):
	right_operand = current_program.operand_stack.pop()
	left_operand = current_program.operand_stack.pop()
	right_type = current_program.type_stack.pop()
	left_type = current_program.type_stack.pop()
	operator = current_program.operator_stack.pop()
	result_type = current_program.sem_cube.get_type(left_type, right_type, operator)
	if result_type != 'error':
		new_temporary_address = current_program.mem.temporary_memory_assign(result_type)
		current_program.func_directory.new_temporary_variable(current_program.scope_l, result_type)
		current_program.quad_number += quad_append(current_program, 
			Quad(current_program.quad_number, operator, left_operand, right_operand, new_temporary_address))
		current_program.operand_stack.append(new_temporary_address)
		current_program.type_stack.append(result_type)
		return 1
	else:
		print('Operation type mismatch at')
		sys.exit()

