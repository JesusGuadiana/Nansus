# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  quadVer.py
#  Last edit: 24/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from functions.evaluateExpression import evaluate_binary_operation, evaluate_binary_operation_array_version
from functions.quadGenerator import quad_append
from structures.quad import Quad
import sys

def quad_ver_function(current_program):
	a = 1
	argument_type = current_program.type_stack.pop()
	if argument_type == 'int':
		argument = current_program.operand_stack.pop()
		if current_program.scope_l == current_program.scope_g:
			current_variable = current_program.func_directory.get_function_variable(
			current_program.scope_g, current_program.current_array_id)
		else:
			current_variable = current_program.func_directory.get_function_variable(
			current_program.scope_l, current_program.current_array_id)
		if current_variable is not None:
			if current_variable['dimension_one'] != -1 and current_variable['dimension_two'] == -1:
				current_program.quad_number += quad_append(current_program,
					Quad(current_program.quad_number, 'VER', argument, 0,
					current_variable['dimension_one']))
				current_program.operand_stack.append(argument)
				k_value = current_program.mem.constant_memory_assign('int', 0)
				current_program.operand_stack.append(k_value)
				current_program.type_stack.append('int')
				current_program.type_stack.append('int')
				current_program.operator_stack.append('+') #This command and the last 4 are for adding -k (0 in this case)
				current_program.quad_number += evaluate_binary_operation(current_program)
				memory_sum = current_program.operand_stack.pop()
				base = current_program.operand_stack.pop()
				dir_base = current_program.mem.constant_memory_assign('int', base) #We store the base address in a variable to add it
				current_program.operand_stack.append(memory_sum)
				current_program.operand_stack.append(dir_base)
				current_program.operator_stack.append('+')
				current_program.quad_number += evaluate_binary_operation_array_version(current_program); #Calls for a list insert into operand stack
			else:
				print("Variable " + current_program.current_id + " is not an array.")
				sys.exit()

		else:
			print("Variable " + current_program.current_id + " is not defined.")
			sys.exit()

def quad_ver_two_function(current_program):
	a = 1
	s2 = 1
	s1 = 1


	s2_type = current_program.type_stack.pop()
	s1_type = current_program.type_stack.pop()
	if s2_type == 'int' and s1_type == 'int':
		s2 = current_program.operand_stack.pop()
		s1 = current_program.operand_stack.pop()
		if current_program.scope_l == current_program.scope_g:
			current_variable = current_program.func_directory.get_function_variable(
			current_program.scope_g, current_program.current_array_id)
		else:
			current_variable = current_program.func_directory.get_function_variable(
			current_program.scope_l, current_program.current_array_id)
		if current_variable is not None:
			if current_variable['dimension_one'] != -1:
				if current_variable['dimension_two'] != -1:
					current_program.quad_number += quad_append(current_program,
						Quad(current_program.quad_number, 'VER', s1, 0,
						current_variable['dimension_one']))
					current_program.operand_stack.append(s1)
					current_program.operand_stack.append(
						current_program.mem.temporary_memory_assign('int', current_variable['dimension_two'])) #S1 * d2
					current_program.type_stack.append('int')
					current_program.type_stack.append('int')
					current_program.operator_stack.append('*')
					current_program.quad_number += evaluate_binary_operation(current_program)
					current_program.quad_number += quad_append(current_program,
						Quad(current_program.quad_number, 'VER', s2, 0,
						current_variable['dimension_two']))
					current_program.operand_stack.append(s2)
					current_program.type_stack.append('int')
					current_program.type_stack.append('int')
					current_program.operator_stack.append('+') #Adds the second index (s2)
					current_program.quad_number += evaluate_binary_operation(current_program)
					current_program.operand_stack.append(current_program.operand_stack.pop())
					k_value = current_program.mem.constant_memory_assign('int', 0)
					current_program.operand_stack.append(k_value) 
					current_program.type_stack.append('int')
					current_program.type_stack.append('int')
					current_program.operator_stack.append('+')  #This command and the last 4 are for adding -k (0 in this case)
					current_program.quad_number += evaluate_binary_operation(current_program)
					memory_sum = current_program.operand_stack.pop()
					base = current_program.operand_stack.pop()
					dir_base = current_program.mem.constant_memory_assign('int', base)
					current_program.operand_stack.append(memory_sum)
					current_program.operand_stack.append(dir_base)
					current_program.operator_stack.append('+')
					current_program.quad_number += evaluate_binary_operation_array_version(current_program); #Calls for a list insert into operand stack
				else:
					print("Variable " + current_program.current_id + " is not a matrix.")
					sys.exit()
			else:
				print("Variable " + current_program.current_id + " is not dimensioned.")
				sys.exit()

		else:
			print("Variable " + current_program.current_id + " is not defined.")
			sys.exit()