from structures.quad import Quad
from functions.printToOutputFile import print_to_output_file
def evaluate_operation(current_program):
	right_operand = current_program.operand_stack.pop()
	right_type = current_program.type_stack.pop()
	left_operand = current_program.operand_stack.pop()
	left_type = current_program.type_stack.pop()
	operator = current_program.operator_stack.pop()
	result_type = current_program.semantic_cube.get_type(left_type, right_type, operator)
	if result_type != 'error':
		new_temporary = current_program.memory.request_temporal_address(result_type)
		current_program.function_directory.new_temporary_variable(current_program.scope_l, result_type)
		quad = Quad(current_program.quad_number, operator, left_operand, right_operand, new_temporary)
		current_program.quad_list.append(quad)
		print_to_output_file(quad)
		current_program.operand_stack.append(new_temporary)
		current_program.type_stack.append(result_type)
	else:
		print('Operation type mismatch at {0}'.format(p.lexer.lineno))
		sys.exit()