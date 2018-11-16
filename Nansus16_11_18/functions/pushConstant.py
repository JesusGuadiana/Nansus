def push_constant_to_stack(current_program, element, c_type):

	address = current_program.mem.constant_exists(c_type, int(element))
	if address is None:
		address = current_program.mem.constant_memory_assign(c_type, int(element))
	current_program.operand_stack.append(address)
	current_program.type_stack.append(c_type)