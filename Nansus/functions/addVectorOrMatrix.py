# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  addVector or Matrix.py
#  Last edit: 19/11/2018
# -----------------------------------------------------------------------------
import sys
def add_vector_or_matrix(current_program):
	exists = current_program.func_directory.function_variable_exists(current_program.scope_l, 
		current_program.current_id)
	if not exists:
		if current_program.scope_l == current_program.scope_g:
			base_address = current_program.mem.sequential_global_assign(current_program.current_type,
				current_program.mem.get_content(current_program.vec_mat_first_dimension) * 
				current_program.mem.get_content(current_program.vec_mat_second_dimension))
		else:
			base_address = current_program.mem.sequential_local_assign(current_program.current_type,
				current_program.mem.get_content(current_program.vec_mat_first_dimension) * 
				current_program.mem.get_content(current_program.vec_mat_second_dimension))		
		current_program.func_directory.new_local_variable(current_program.scope_l, current_program.current_type,
		current_program.current_id, base_address)
	else:
		print("Variable" + current_program.current_id + "already exists in this context.")
		sys.exit()



	