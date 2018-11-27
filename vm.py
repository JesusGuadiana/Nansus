# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  vm.py
#  Last edit: 21/11/2018
# -----------------------------------------------------------------------------
from functions.turtleFunctions import Jedo
from memory.memoryInterface import MemInterface
from structures.funcDirectory import FuncDirectory
from ast import literal_eval
import sys
import pprint

class Machine():

	def __init__(self, quads, memory, funcDirectory):
		self.quads = quads;
		self.total_quads = len(quads);
		self.current_quad = 0;
		self.memory = memory;
		self.funcDirectory = funcDirectory

	def request_local_addresses(self, function):
		for i in range(function['function']['local_variable_counter']['int']):
			function['memory'].local_memory_assign('int')
		for i in range(function['function']['local_variable_counter']['float']):
			function['memory'].local_memory_assign('float')
		for i in range(function['function']['local_variable_counter']['char']):
			function['memory'].local_memory_assign('char')

	def request_temporal_addresses(self, function):
		for i in range(function['function']['temporary_variable_counter']['int']):
			function['memory'].temporary_memory_assign('int')
		for i in range(function['function']['temporary_variable_counter']['float']):
			function['memory'].temporary_memory_assign('float')
		for i in range(function['function']['temporary_variable_counter']['char']):
			function['memory'].temporary_memory_assign('char')
		for i in range(function['function']['temporary_variable_counter']['bool']):
			function['memory'].temporary_memory_assign('bool')

	def literal_eval_helper(self, type):
		if type == "<class 'int'>":
			type == "int"


	def run_machine(self):
		pp = pprint.PrettyPrinter(indent=4)

		memory = self.memory
		function = {}
		paramters = 0
		local_segment_pointer_list = []
		temporal_segment_pointer_list = []
		instruction_number_to_back_list = []

		while self.current_quad < self.total_quads:
			quad = self.quads[self.current_quad]

			operator = quad.operator
			l_address = quad.left_operand
			r_address = quad.right_operand
			result_address = quad.result

			# print(function)

			#SPECIAL FUNCTIONS
			#Creates jedo object with speed slow and increments current_quad
			if operator == "create":
				jedo = Jedo("slow")
				self.current_quad += 1
			#If the operator in the quad contains "circle"
			elif operator == "circle":
				#Get the value inside the memory address in the l_address
				#Send left_operand (circle radius) as parameter to the function circle
				left_operand = memory.get_content(l_address)
				jedo.circle(left_operand)
				#Procced to the next quad
				self.current_quad += 1
			elif operator == "arch":
				#Get the value inside l_address which represents the size of the arch7
				#Trim " " from the string in the r_address which represents arch to the right or to the left
				left_operand = memory.get_content(l_address)
				r_string = r_address.replace('"',"")
				#if r_string is right perfom an arch to the right of jedo
				if r_string == "right":
					jedo.turnRight(90)
					#Performs a semi circle with the size given by the user (left operand)
					jedo.circle(left_operand, 180)
					jedo.turnRight(90)
				#if r_string is left perfomr an arch to the left of jedo
				elif r_string == "left":
					jedo.turnRight(90)
					#Performs a semi circle with the size given by the user (left operand)
					jedo.circle(left_operand, -180)
					jedo.turnRight(90)

				self.current_quad += 1
			#Creates a square in the turtle interface
			elif operator == "square":
				#Get the content in l_address and insert it as parameter in the square function
				left_operand = memory.get_content(l_address)

				jedo.square(left_operand)
				self.current_quad += 1
			elif operator == "triangle":
				#Get the content in l_address and insert it as parameter in the triangle function
				left_operand = memory.get_content(l_address)
				jedo.triangle(left_operand)
				self.current_quad += 1
			#Creates a rectangle in the turtle interface
			elif operator == "rectangle":
				#Get the content in l_addres and r_address
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(l_address)
				#Perform a square x = left_operand, y = right_operand
				jedo.rectangle(left_operand, right_operand)
				self.current_quad += 1
			#Makes turtle move forward x steps
			elif operator == "forward":
				#Get the content in l_address
				left_operand = memory.get_content(l_address)
				#Move forward x positions
				jedo.forward(left_operand);

				self.current_quad += 1
			elif operator == "back":
				#Get the content in l_address
				left_operand = memory.get_content(l_address)
				#Move backwards x positions
				jedo.back(left_operand)
				self.current_quad += 1
			#Turtle turns right x degrees
			elif operator == "turnRight":
				left_operand = memory.get_content(l_address)

				jedo.right(left_operand)
				self.current_quad += 1
			#Turtle turns left x degrees
			elif operator == "turnLeft":
				left_operand = memory.get_content(l_address)

				jedo.left(left_operand)
				self.current_quad += 1
			#Changes turtles's color to x color
			elif operator == "color":
				left_operand = memory.get_content(l_address)
				left_operand = left_operand.replace('"',"")

				jedo.color(left_operand)
				self.current_quad += 1
			#changes pen's thichkness
			elif operator == "thickness":
				left_operand = memory.get_content(l_address)

				jedo.thickness(left_operand)
				self.current_quad += 1
				#---------------------------------------NEW SPECIAL FUNCTION (DOCUMENTATION REQUIRED) -------------------------------
			#Draws a dot with x radius and y color
			elif operator == "drawDot":
				#Get the content in l_addres which represents the radius value
				left_operand = memory.get_content(l_address)
				#Get the string color in the r_address and trim "" values
				right_operand = r_address;
				right_operand = right_operand.replace('"',"")

				jedo.drawDot(left_operand, right_operand)
				self.current_quad += 1
			#Enables turtle to draw on movement
			elif operator == "startpen":
				jedo.startPen()

				self.current_quad += 1
			#Turtle is not able to draw
			elif operator == "stoppen":
				jedo.stopPen()

				self.current_quad += 1
			#Tells turtle that an object will be filled with a color
			elif operator == "startfill":
				jedo.startFill()

				self.current_quad += 1
			#Tells the turtle what color to fill the shape with
			elif operator == "fillshape":
				#Get the color in string format
				left_operand = memory.get_content(l_address)
				left_operand = left_operand.replace('"',"")
				#fill the shape with the given color
				jedo.fillShape(left_operand)

				self.current_quad += 1
			#Tells the turtle to stop the fill"
			elif operator == "stopfill":
				jedo.stopFill()

				self.current_quad += 1
			#Restar turtle interface
			elif operator == "restart":
				jedo.restart()

				self.current_quad += 1
			#Execute the + operation for incoming quad
			elif operator == "+":
				#Gets the left and right values to add
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])
				#Performs the SUM action
				result = right_operand + left_operand
				#Store the result of the operation on the result address given by the quad
				memory.edit_memory_content(result_address, result)
				self.current_quad += 1
			elif operator == "=":
				#Get the value in the l_address
				result_address2 = 0;
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(result_address, list):
					result_address2 = memory.get_content(result_address[-1])
				else:
					result_address2 = result_address
				#Store the value in left_operand
				memory.edit_memory_content(result_address2, left_operand)
				self.current_quad += 1
			#Execute the - operation for incoming quad
			elif operator == "-":
				#Get the left and right values and perform the subtraction
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])

				#Store the result of the - operation
				result = left_operand - right_operand
				#store the result of the operation in the result_address
				memory.edit_memory_content(result_address, result)
				self.current_quad += 1
			#Execute the * operation for incoming quad
			elif operator == "*":
				#Get the left and right values and perform the multiplication
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])

				result = right_operand * left_operand
				#Store the result in the result_address
				memory.edit_memory_content(result_address, result)
				self.current_quad += 1
			#Execute the / operation for incoming quad
			elif operator == "/":
				#Get the left and right values and perform the division
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])

				#if the right operand is 0 raise an error and exit program
				if right_operand == 0:
					print ('ZeroDivisionError: division by zero')
					sys.exit()
				else:
					#Else perform the division
					result = left_operand / right_operand
				#Store the result in the result_address
				memory.edit_memory_content(result_address, result)
				self.current_quad +=1
			#Execute the == operation for the incomig quad
			elif operator == "==":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])
				#Perform the == operation and get the result
				boolean_result = left_operand == right_operand
				#return 1 or 0 to represent booleans
				if boolean_result == True:
					result = 1
				else:
					result = 0
				#Store the result in the result_address
				memory.edit_memory_content(result_address, result)
				self.current_quad += 1
			elif operator == "<":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])
				#Perform the < operation and store the result
				boolean_result = left_operand < right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(result_address, result)
				self.current_quad += 1
			#Execute the > operation
			elif operator == ">":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])
				#Perform the > operation and store the result
				boolean_result = left_operand > right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(result_address, result)
				self.current_quad += 1
			#Execure the >= operation for the incoming quad
			elif operator == ">=":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])
				#Perform the >= operation and store the result
				boolean_result = left_operand >= right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(result_address , result)
				self.current_quad += 1
			#Execute the <= operation for the incoming quad
			elif operator == "<=":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])
				#Perform the <= operation and store the result
				boolean_result = left_operand <= right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(result_address , result)
				self.current_quad += 1
			#Execute the != operation for the incomign quad
			elif operator == "!=":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])
				#Perform the != operation and store the result
				boolean_result = left_operand != right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(result_address, result)
				self.current_quad += 1
			elif operator == "&&":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])
				#Perform the $$ operation and store the result
				boolean_result = left_operand and right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(result_address, result)
				self.current_quad += 1
			elif operator == "||":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				if isinstance(r_address, list):
					right_operand = memory.get_content(memory.get_content(r_address[-1]))
				else:
					right_operand = memory.get_content(r_address)
				if isinstance(result_address, list):
					result_address = memory.get_content(r_address[-1])
				#Perform the || operation and store the result
				boolean_result = left_operand or right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(result_address, result)
				self.current_quad += 1
			#Execute the print operation for the incoming quad
			elif operator == "PRINT":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				#Print the l_address content
				print(str(left_operand))
				self.current_quad += 1
			elif operator == "GOTO":
				#Redirect current_quad to the quad number in the result_address
				self.current_quad = result_address - 1
			#GOTOF operation
			elif operator == "GOTOF":
				left_operand = memory.get_content(l_address)
				if not left_operand:
					self.current_quad = result_address - 1
				else:
					self.current_quad += 1
			elif operator == "GOTOV":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				#If left operand = 1 "true" return tu quad
				if left_operand == 1:
					self.current_quad = result_address - 1
				else:
				#Else advance
					self.current_quad += 1
			elif operator == "ENDPROC":
				function.clear()
				memory.local_memory = local_segment_pointer_list.pop()
				memory.temporal_memory = temporal_segment_pointer_list.pop()

				self.current_quad = instruction_number_to_back_list.pop() + 1
			elif operator == "ERA":
				#Get the function's info and assign memory for its variables
				function['function'] = self.funcDirectory.get_function(l_address)
				function['memory'] = MemInterface()
				parameters = 0

				#Saves the local and temporaral variables of the function
				self.request_local_addresses(function)
				self.request_temporal_addresses(function)
				self.current_quad += 1
			elif operator == "GOSUB":
				 # Stores the number of instruction we will return after the function execution ends
				instruction_number_to_back_list.append(self.current_quad)

                # Change the local and temporal memory segments for the ones the in the function
				local_segment_pointer_list.append(memory.local_memory)
				temporal_segment_pointer_list.append(memory.temporary_memory)

				memory.local_memory = function['memory'].local_memory
				memory.temporary_memory = function['memory'].temporary_memory

				self.current_quad = result_address - 1
			elif operator == "PARAMETER":
                # Gets the value of the parameter
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				#Get the address of the parameter
				parameter_address = function['function']['parameters']['parameter_addresses'][parameters]
				#Increment parameter counter
				parameters += 1
				#Edit the parameter_address with the new parameter value
				function['memory'].edit_memory_content(parameter_address, left_operand)
				self.current_quad += 1
			elif operator == "RETURN":
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				memory.edit_memory_content(result_address, left_operand)

				self.current_quad += 1
			elif operator == "VER":
				#Get the index to get and the limits of the dimentioned variable
				if isinstance(l_address, list):
					left_operand = memory.get_content(memory.get_content(l_address[-1]))
				else:
					left_operand = memory.get_content(l_address)
				lower_limit = r_address
				upper_limit = result_address
				#Check if the value is within the limits of the dimentioned variable
				if left_operand >= lower_limit and left_operand < upper_limit:
					self.current_quad += 1
				else:
					print("Index out of bounds")
					sys.exit()

			elif operator =="READINPUT":
				#Reads the input and stores the value in memory
				var_type = l_address

				user_var = input()
				user_var_type = ""
				try:
					user_var_type = type(literal_eval(user_var))
					if user_var_type == type(literal_eval("1")):
						user_var_type = "int"
						user_var = int(user_var)
					elif user_var_type == type(literal_eval("1.0")):
						user_var_type = "float"
						user_var = float(user_var)
				except(ValueError, SyntaxError):
					if len(user_var) == 1:
						user_var_type = "char"
						user_var = char(user_var)
				if var_type == user_var_type:
					memory.edit_memory_content(result_address, user_var)
				else:
					print("Expected type " +  var_type + " variable")
					sys.exit()

				self.current_quad += 1;
