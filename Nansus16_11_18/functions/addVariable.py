def add_variable_to_directory(current_program):
	exists = current_program.func_directory.function_variable_exists(current_program.scope_l, 
		current_program.current_id)
	if not exists:
		if current_program.scope_l == current_program.scope_g:
			new_address = current_program.mem.global_memory_assign(current_program.current_type)
		else:
			new_address = current_program.mem.local_memory_assign(current_program.current_type)			
		current_program.func_directory.new_local_variable(current_program.scope_l, 
			current_program.current_type, current_program.current_id, new_address)