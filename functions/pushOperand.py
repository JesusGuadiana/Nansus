import sys

def push_operand_to_stack(current_program, identifier, index = 0):
	#if current_program.current_dim == 0:
		operand = current_program.func_directory.get_function_variable(current_program.scope_l, identifier)
		if operand is None:
			operand = current_program.func_directory.get_function_variable(current_program.scope_g, identifier)
			if operand is not None:
				current_program.operand_stack.append(variable['address'])
				current_program.type_stack.append(variable['type'])
			else:
				print("Variable " + identifier + " is not declared in this scope.")
				sys.exit()
			
		else:
			current_program.operand_stack.append(variable['address'])
			current_program.type_stack.append(variable['type'])
	#else:
	#	operand = current_program.func_directory.get_vector_or_matrix_index(current_program.scope_l, identifier, index)
	#	if operand is None:
	#		operand = current_program.func_directory.get_vector_or_matrix_index(current_program.scope_g, identifier, index)
	#		if operand is not None:
	#			current_program.operand_stack.append(variable['address'])
	#			current_program.type_stack.append(variable['type'])
	#		else:
	#			print("Variable " + identifier + " is not declared in this scope.")
	#			sys.exit()
	#		
	#	else:
	#		current_program.operand_stack.append(variable['address'])
	#		current_program.type_stack.append(variable['type'])