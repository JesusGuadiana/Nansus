# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  functionReturn.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from functions.quadGenerator import quad_append
from structures.quad import Quad

def return_from_function(current_program):
	return_value = current_program.operand_stack.pop()
	return_type = current_program.type_stack.pop()
	function = current_program.func_directory.get_function(current_program.scope_l)
	function_type = function['return_type']
	function_ret_address = function['return_address']
	if function_type == return_type:
		#This line should be properly providing the return address for the function (but it doesn't work at the moment)
		current_program.quad_number += quad_append(current_program,
			Quad(current_program.quad_number, 'RETURN', return_value, None, function_ret_address))
	else:
		print("Function return type mismatch.")
		sys.exit()
