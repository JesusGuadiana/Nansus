from structures.quad import Quad
from functions.printToOutputFile import *

def goto_main_quad(quad_number, quad_list):
	print_to_output_file("\n\nINTERMEDIATE CODE:\n")
	current_quad = Quad(quad_number,'GOTO', 'MAIN', None, None)
	quad_list.append(current_quad)
	print_to_output_file(current_quad)