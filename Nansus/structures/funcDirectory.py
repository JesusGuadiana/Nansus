# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language
#  funcDirectory.py
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
#Packages Imported 
from structures.varTable import VarTable
from functions.printToOutputFile import print_to_output_file
import json

#Class Name
class FuncDirectory():

	#Base Constructor
	def __init__(self):
		self.list_of_functions = {}

	#FuncDirectory attribute definition
	def new_function(self, identifier, return_type, quad_number = -1):
		
		self.list_of_functions[identifier] = {
		
		'identifier' : identifier,

		'parameters' : {
			'parameter_types' : [],
			'parameter_addresses' : [],
			'parameter_counter' : 0
		},

		'local_variables' : VarTable(),

		'local_variable_counter' : {
		'int' : 0,
		'float' : 0,
		'char' : 0,
		},

		'temporary_variable_counter' : {
		'int' : 0,
		'float' : 0,
		'char' : 0,
		'bool' : 0
		},

		'return_type' : return_type,
		'return_address' : -1,
		'quad_number' : quad_number
		}

	#Verification of existance/non-existance prior to interacting with specified function
	def function_exists(self, identifier):
		return identifier in self.list_of_functions.keys()

	#Getter for the specified function
	def get_function(self, identifier):
		if self.function_exists(identifier):
			return self.list_of_functions[identifier]
		else:
			print("Function " + identifier + " does not exist.")
			return None

	#Adds each parameter (one by one) as they are read in the syntactical analyzer for the specified function
	def new_function_parameter(self, identifier, p_type, p_address):
		current_function = self.get_function(identifier)
		if current_function is not None:
			current_function['parameters']['parameter_types'].append(p_type)
			current_function['parameters']['parameter_addresses'].append(p_address)
			current_function['parameters']['parameter_counter'] += 1
		else:
			print("Function " + identifier + " does not exist.")





	#Function Directory's version of variable existance check from VarTable
	def function_variable_exists(self, identifier, v_identifier):
		new_function = self.get_function(identifier)
		if new_function is not None:           
			if new_function['local_variables'].variable_exists(v_identifier):
				return True
			else:
				return False
		else:
			print("Variable name already in use. (Come on, be creative.)")

	#Adds a new local variable (a non-dimensioned variable) to the specified function
	#Local means "current active context" in my head in this context - Juan Fernando Ulloa 
	def new_local_variable(self, identifier, v_type, v_identifier, v_address = 0):
		new_function = self.get_function(identifier)
		if new_function is not None:
			if not new_function['local_variables'].variable_exists(v_identifier):
				new_function['local_variables'].new_variable(v_type, v_identifier, v_address)
				new_function['local_variable_counter'][v_type] += 1;
			else:
				print("Variable name already in use. (Come on, be creative.)")
		else:
			print("Function " + identifier + " does not exist.")

	def set_local_variable_dimension_one(self, identifier, v_type, v_identifier, v_address = 0):
		current_function = self.get_function(identifier)
		if current_function is not None:
			if current_function['local_variables'].variable_exists(v_identifier):
				current_function['local_variables'].set_dimension_one(v_identifier, 
					v_address)
			else:
				print("Variable name already in use. (Come on, be creative.)")
		else:
			print("Function " + identifier + " does not exist.")

	def set_local_variable_dimension_one(self, identifier, v_type, v_identifier, v_address = 0):
		current_function = self.get_function(identifier)
		if current_function is not None:
			if current_function['local_variables'].variable_exists(v_identifier):
				current_function['local_variables'].set_dimension_two(v_identifier, 
					v_address)
			else:
				print("Variable " + v_identifier + "does not exist in this context.")
		else:
			print("Function " + identifier + " does not exist.")

	#Adds to the temporary variable counter
	def new_temporary_variable(self, identifier, t_type):
		new_function = self.get_function(identifier)
		if new_function is not None:
			new_function['temporary_variable_counter'][t_type] += 1        
		else:
			print ("Function " + identifier + " does not exist.")





	#From this point on, these functions are either simple getters, or simple setters
	#Type Getter for the specified function return type
	def get_function_type(self, identifier):
		current_function = self.get_function(identifier)
		if current_function is not None:
			current_function = current_function['return_type']
			return current_function
		else:
			print ("Function " + identifier + " does not exist.")

	#Parameter List of Types and Address Getter for the specified function
	def get_function_parameters(self, identifier):
		current_function = self.get_function(identifier)
		if current_function is not None:
			return current_function['parameters']
		else:
			print ("Function " + identifier + " does not exist.")

	#Variable Getter for single specified variable
	def get_function_variable(self, identifier, v_identifier):
		current_function = self.get_function(identifier)
		if current_function is not None:        
			current_variable = current_function['local_variables'].get_variable(v_identifier)
			if current_variable is not None:              
				return current_variable
			else:
				#print ("Variable " + str(current_variable) + " was not declared in this scope.")
				return None
		else:
			print ("Function " + identifier + " does not exist.") 

	#Function Quadruple Getter for specified function
	def get_quad_number(self, identifier):
		new_function = self.get_function(identifier)
		if new_function is not None:  
			return new_function['quad_number']        
		else:
			print ("Function " + identifier + " does not exist.")   

	




	#Function Quadruple Setter for specified function
	def set_quad_number(self, identifier, quad_number):
		current_function = self.get_function(identifier)
		if current_function is not None:
			current_function['quad_number'] = quad_number
		else:
			print ("Function " + identifier + " does not exist.")

	#Function Address Setter for specified function
	def set_function_address(self, identifier, address):
		current_function = self.get_function(identifier)
		if current_function is not None:
			current_function['return_address'] = address
		else:
			print ("Function " + identifier + " does not exist.")

	def print_directory(self):
		for function, properties in self.list_of_functions.items():
			print_to_output_file("\n")
			print_to_output_file("function : " + str(function))
			for prop, value in properties.items():
				if isinstance(value, VarTable):
					print_to_output_file("  " + str(prop) + " : " +
						json.dumps(value.list_of_variables, indent=4))
				elif isinstance(value, dict):
					print_to_output_file("  " + str(prop) + " : " +
						json.dumps(value, indent=4))
				else:
					print_to_output_file("  " + str(prop) + " : " + str(value))

			print_to_output_file("-" * 80)