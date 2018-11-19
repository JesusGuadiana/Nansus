# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  pushId.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
import sys
def push_id_to_stack(current_program, v_name):
	identifier = current_program.func_directory.get_function_variable(current_program.scope_l, v_name)
	if identifier is None:
		identifier = current_program.func_directory.get_function_variable(current_program.scope_g, v_name)
		if identifier is not None:
			current_program.type_stack.append(identifier['type'])
			current_program.operand_stack.append(identifier['address'])
		else:
			print("The variable " + v_name + " has not been declared.")
			sys.exit()
	else:
		current_program.operand_stack.append(identifier['address'])
		current_program.type_stack.append(identifier['type'])