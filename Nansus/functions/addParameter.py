# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  addParameter.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
def add_parameter_to_function(current_program, identifier):
	new_param_address = current_program.mem.local_memory_assign(current_program.current_type)
	current_program.func_directory.new_local_variable(current_program.scope_l, current_program.current_type, 
		identifier, new_param_address)
	current_program.func_directory.new_function_parameter(current_program.scope_l, current_program.current_type, 
		new_param_address)

		

