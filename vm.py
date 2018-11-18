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
			if operator == "circle":
				left_operand = memory.get_content(l_address)

				jedo.circle(left_operand)
				self.current_quad += 1
			elif operator == "square":
				left_operand = memory.get_content(l_address)

				jedo.square(left_operand)
				self.current_quad += 1
			elif operator == "rectangle":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(l_address)

				jedo.rectangle(left_operand, right_operand)
				self.current_quad += 1
			elif operator == "forward":
				left_operand = memory.get_content(l_address)
				jedo.forward(left_operand);

				self.current_quad += 1
			elif operator == "back":
				left_operand = memory.get_content(l_address)

				jedo.back(left_operand)
				self.current_quad += 1
			elif operator == "turnRight":
				left_operand = memory.get_content(l_address)

				jedo.right(left_operand)
				self.current_quad += 1
			elif operator == "turnLeft":
				left_operand = memory.get_content(l_address)

				jedo.left(left_operand)
				self.current_quad += 1
			elif operator == "color":
				left_operand = memory.get_content(l_address)

				jedo.color(left_operand)
				self.current_quad += 1
			elif operator == "thickness":
				left_operand = memory.get_content(l_address)

				jedo.thickness(left_operand)
				self.current_quad += 1
				#---------------------------------------FUNCIONES NUEVAS DE TURTLE NO DECLARADAS EN LA PROPUESTA -------------------------------
			elif operator == "drawDot":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				jedo.drawDot(left_operand, right_operand)
				self.current_quad += 1
			elif operator == "startPen":
				jedo.startPen()

				self.current_quad += 1
			elif operator == "stopPen":
				jedo.stopPen()

				self.current_quad += 1
			elif operator == "startFill":
				jedo.startFill()

				self.current_quad += 1
			elif operator == "fillShape":
				left_operand = memory.get_content(l_address)
				jedo.fillShape(left_operand)

				self.current_quad += 1
			elif operator == "stopFill":
				jedo.stopFill()

				self.current_quad += 1
			elif operator == "restart":
				jedo.restart()

				self.current_quad += 1
			elif operator == "+":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				result = right_operand + left_operand

				memory.edit_memory_content(resultAddress, result)
				self.current_quad += 1
			elif operator == "-":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				result = right_operand - left_operand

				memory.edit_memory_content(resultAddress, result)
				self.current_quad += 1
			elif operator == "*":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				result = right_operand * left_operand

				memory.edit_memory_content(resultAddress, result)
				self.current_quad += 1
			elif operator == "/":
				left_operand = memory.get_content(l_address)
				right_operand = memory.get_content(r_address)

				if right_operand == 0:
					print 'ZeroDivisionError: division by zero'

				result = left_operand / right_operand
				memory.edit_memory_content(resultAddress, result)
				self.current_quad +=1
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
			elif operator == "print":
				left_operand = memory.get_content(l_address)

				print str(left_operand)
				self.current_quad += 1
			elif operator == "goto":
				self.current_quad = result_address
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
