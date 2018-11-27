# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  gotoElse.py
#  Last edit: 21/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from functions.evaluateExpression import evaluate_binary_operation
from functions.quadGenerator import quad_append
from structures.quad import Quad
def goto_else_function(current_program):
	end = current_program.jump_stack.pop();
	#GOTO's are empty at creation
	current_program.quad_number += quad_append(current_program,
	 Quad(current_program.quad_number, "GOTO", None, None, None))
	quad = current_program.quad_list[end]
	end = current_program.jump_stack.append(current_program.quad_number-2);
	quad.set_quad_goto(current_program.quad_number)