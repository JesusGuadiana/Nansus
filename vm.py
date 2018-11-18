from turtle_functions import Jedo

class Machine():

	def __init__(self, quads, memory):
		self.quads = quads;
		self.total_quads = len(quads);
		self.current_quad = 1;
		self.memory = memory;


	def run_machine(self):

		while self.current_quad < self.total_quads:
			quad = self.quads[self.current_quad];
			memory = self.memory

			operator = quad.operator
			l_address = quad.left_operand
			r_address = quad.right_operand
			result_address = quad.result

			if (self.current_quad == 1):
				jedo = Jedo("slow")

			#SPECIAL FUNCTIONS
			#Creates a circle in the turtle interface
			if operator == "circle":
				left_operand = memory.get_content(l_address)

				jedo.circle(left_operand)
				self.current_quad += 1
			#Creates a square in the turtle interface
			elif operator == "square":
				left_operand = memory.get_content(l_address)

				jedo.square(left_operand)
				self.current_quad += 1
			#Creates a rectangle in the turtle interface
			elif operator == "rectangle":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(l_address)

				jedo.rectangle(left_operand, right_operand)
				self.current_quad += 1
			#Makes turtle move forward x steps
			elif operator == "forward":
				left_operand = memory.get_content(l_address)
				jedo.forward(left_operand);

				self.current_quad += 1
			elif operator == "back":
			#Turtle moves backwards
				left_operand = memory.get_content(l_address)

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
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				jedo.drawDot(left_operand, right_operand)
				self.current_quad += 1
			#Enables turtle to draw on movement
			elif operator == "startPen":
				jedo.startPen()

				self.current_quad += 1
			#Turtle is not able to draw
			elif operator == "stopPen":
				jedo.stopPen()

				self.current_quad += 1
			#Tells turtle that an object will be filled with a color
			elif operator == "startFill":
				jedo.startFill()

				self.current_quad += 1
			#Tells the turtle what color to fill the shape with
			elif operator == "fillShape":
				left_operand = memory.get_content(l_address)
				jedo.fillShape(left_operand)

				self.current_quad += 1
			#Tells the turtle to stop the fill"
			elif operator == "stopFill":
				jedo.stopFill()

				self.current_quad += 1
			#Restar turtle interface
			elif operator == "restart":
				jedo.restart()

				self.current_quad += 1
			#Execute the + operation for incoming quad
			elif operator == "+":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				result = right_operand + left_operand

				memory.edit_memory_content(resultAddress, result)
				self.current_quad += 1
			#Execute the - operation for incoming quad
			elif operator == "-":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				result = right_operand - left_operand

				memory.edit_memory_content(resultAddress, result)
				self.current_quad += 1
			#Execute the * operation for incoming quad
			elif operator == "*":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				result = right_operand * left_operand

				memory.edit_memory_content(resultAddress, result)
				self.current_quad += 1
			#Execute the / operation for incoming quad
			elif operator == "/":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				if right_operand == 0:
					print 'ZeroDivisionError: division by zero'

				result = left_operand / right_operand
				memory.edit_memory_content(resultAddress, result)
				self.current_quad +=1
			#Execute the == operation for the incomig quad
			elif operator == "==":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				boolean_result = left_operand == right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(resultAddress, result)
				self.current_quad += 1
			#Execute the < operation for the incoming quad
			elif operator == "<":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				boolean_result = left_operand < right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(resultAddress, result)
				self.current_quad += 1
			#Execute the > operation
			elif operator == ">":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				boolean_result = left_operand > right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(resultAddress, result)
				self.current_quad += 1
			#Execure the >= operation for the incoming quad
			elif operator == ">=":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				boolean_result = left_operand >= right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(resultAddress , result)
				self.current_quad += 1
			#Execute the <= operation for the incoming quad
			elif operator == "<=":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				boolean_result = left_operand <= right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(resultAddress , result)
				self.current_quad += 1
			#Execute the != operation for the incomign quad
			elif operator == "!=":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				boolean_result = left_operand != right_operand

				if boolean_result == True:
					result = 1
				else:
					result = 0

				memory.edit_memory_content(resultAddress, result)
				self.current_quad += 1
			#Execute the print operation for the incoming quad
			elif operator == "print":
				left_operand = memory.get_content(l_address)

				print str(left_operand)
				self.current_quad += 1
			#GOTO operation
			elif operator == "goto":
				self.current_quad = result_address
			#GOTOF operation
			elif operator == "gotof":
				left_operand = current_memory.get_value(left_operand_address)

				if not left_operand:
					self.current_quad = result_address
				else:
					self.current_quad += 1
			elif operator == "ver"
			elif operator == "era"
			elif operator == "param"
			elif opertaor == "gosub"
			elif operator == "endproc"
			elif operator == "return"
			elif operator == "read"
