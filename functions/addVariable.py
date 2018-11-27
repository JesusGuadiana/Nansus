# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  addVariable.py
#  Last edit: 19/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
import sys

def add_variable_to_directory(current_program):
	#Verifies that the function exists, then determines scope, then finally assigns a memory to the variable
	exists = current_program.func_directory.function_variable_exists(current_program.scope_l, 
		current_program.current_id)
	if not exists:
		if current_program.scope_l == current_program.scope_g:
			new_address = current_program.mem.global_memory_assign(current_program.current_type)
		else:
			new_address = current_program.mem.local_memory_assign(current_program.current_type)			
		current_program.func_directory.new_local_variable(current_program.scope_l, 
			current_program.current_type, current_program.current_id, new_address)
	else:
		print("Variable " + current_program.current_id + " already exists in this context.")
		sys.exit()