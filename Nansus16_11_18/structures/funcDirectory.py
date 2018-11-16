# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language Function Directory
#  Last edit: 14/11/2018
# -----------------------------------------------------------------------------
#Packages Imported 
from structures.varTable import VarTable

#Class Name
class FuncDirectory():

	#Base Constructor
	def __init__(self):
		self.list_of_functions = {}

	#FuncDirectory attribute definition
	def new_function(self, identifier, ret_type, list_of_parameters = [], 
		addresses_for_parameters = []):
		
		self.list_of_functions[identifier] = {
		'identifier' : identifier,

		'parameters' : {
			'parameter_types' : list_of_parameters,
			'parameter_addresses' : addresses_for_parameters,
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
		},

		'return_address' : -1,
		'quad_number' : -1
		}

	#Getter for the specified function
	def get_function(self, identifier):
		if self.function_exists(identifier):
			return self.list_of_functions[identifier]
		else:
			print("Function " + identifier + " does not exist.")
			return None

	#Verification of existance/non-existance prior to interacting with specified function
	def function_exists(self, identifier):
		return identifier in self.list_of_functions.keys()

	#Adds each parameter (one by one) as they are read in the syntactical analyzer for the specified function
	def new_function_parameter(self, identifier, p_type, p_address):
		new_function = self.get_function(identifier)
		if new_function is not None:
			new_function['parameters']['parameter_types'].append(p_type)
			new_function['parameters']['parameter_addresses'].append(p_address)
		else:
			print("Function " + identifier + " does not exist.")

	#Adds a new local variable (a non-dimensioned variable) to the sepcified function
	def new_local_variable(self, identifier, v_type, v_identifier, v_address = 0):
		new_function = self.get_function(identifier)
		if new_function is not None:
			if not new_function['local_variables'].variable_exists(v_identifier):
				new_function['local_variables'].new_variable(v_type, v_identifier, v_address)
				new_function['local_variable_counter'][v_type] += 1;
			else:
				print("Variable name already in use. (Come on, be creative.)")
		
	#Adds a new 1 or 2 dimension variable to the VarTable for the specified function
	def new_vector_or_matrix(self, identifier, v_identifier):
		new_function = self.get_function(identifier)
		if new_function is not None:
			if new_function['local_variables'].variable_exists(v_identifier['identifier']):
				new_function['local_variables'].new_variable_vector_or_matrix(v_identifier)
			else:
				print("Variable name already in use. (Come on, be creative.)")          
		else:
			print ("Function " + identifier + " does not exist.")

	#Adds to the temporary variable counter
	def new_temporary_variable(self, identifier, t_type):
		new_function = self.get_function(new_function)
		if new_function is not None:
			funct['number_of_temp_variables'][temp_type] += 1        
		else:
			print ("Function " + identifier + " does not exist.")

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


	#From this point on, these functions are either simple getters, or simple setters
	#Type Getter for the specified function identifier
	def get_function_type(self, identifier):
		new_function = self.get_function(identifier)
		if new_function is not None:
			new_function = new_function['return_type']
			return new_function
		else:
			print ("Function " + identifier + " does not exist.")

	#Parameter List of Types and Address Getter for the specified function
	def get_function_parameters(self, identifier):
		new_function = self.get_function(identifier)
		if new_function is not None:
			return new_function['parameters']
		else:
			print ("Function " + identifier + " does not exist.")

	#Variable Getter for single specified variable
	def get_function_variable(self, identifier, v_identifier):
		new_function = self.get_function(identifier)
		if new_function is None:        
			v_identifier = new_function['variables'].get_variable(v_identifier)
			if v_identifier is not None:                
				return v_identifier
			else:
				print ("Variable " + v_identifier + " was not declared in this scope.")
				return None
		else:
			print ("Function " + identifier + " does not exist.") 

	#Function Quadruple Getter for specified function
	def get_quad_number(self, identifier):
		new_function = self.get_function(identifier)
		if new_function is None:  
			return new_function['quad_number']        
		else:
			print ("Function " + identifier + " does not exist.")   

	#Gets the virtual address for a 1 or 2 dimension variable index
	#def get_vector_or_matrix_index(self, identifier, v_identifier, index):
	#	current_function = self.get_function(identifier)
	#	if current_function is not None:
	#		if current_function['local_variables'].variable_exists(v_identifier['identifier']):
	#			current_function['local_variables'].get_variable_vector_or_matrix(v_identifier, index)
	#		else:
	#			print("Variable " + v_identifier + " was not declared in this scope.")          
	#	else:
	#		print ("Function " + identifier + " does not exist.")

	#Function Quadruple Setter for specified function
	def set_quad_number(self, identifier, quad_number):
		current_function = self.get_function(identifier)
		if current_function is None:
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