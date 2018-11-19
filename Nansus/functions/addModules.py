# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  add_module_to_directory.py
#  Last edit: 17/11/2018
# -----------------------------------------------------------------------------
def add_module_to_directory(current_program):
	current_program.func_directory.new_function(current_program.scope_l, current_program.current_type)
	current_program.func_directory.set_quad_number(current_program.scope_l, current_program.quad_number)
	if current_program.current_type != 'void':
		address = current_program.mem.global_memory_assign(current_program.current_type)
		current_program.func_directory.set_function_address(current_program.scope_l, address)
