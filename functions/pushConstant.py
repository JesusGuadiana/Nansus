# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  pushConstant.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
def push_constant_to_stack(current_program, element, c_type):

	#Constants are weird to enter, but they must be validated before entering
	if c_type == 'int':
		constant_address = current_program.mem.constant_exists(c_type, int(element))
		if constant_address is None:
			constant_address = current_program.mem.constant_memory_assign(c_type, int(element))
		current_program.operand_stack.append(constant_address)
		current_program.type_stack.append(c_type)
	elif c_type == 'float':
		constant_address = current_program.mem.constant_exists(c_type, float(element))
		if constant_address is None:
			constant_address = current_program.mem.constant_memory_assign(c_type, float(element))
		current_program.operand_stack.append(constant_address)
		current_program.type_stack.append(c_type)
	elif c_type == 'char':
		constant_address = current_program.mem.constant_exists(c_type, char(element))
		if constant_address is None:
			constant_address = current_program.mem.constant_memory_assign(c_type, char(element))
		current_program.operand_stack.append(constant_address)
		current_program.type_stack.append(c_type)