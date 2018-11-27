# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language 
#  memoryInterface.py
#  (Program Information interacts with memory through this class)
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
#Libraries imported
from memory.memoryManager import MemManager
import sys

#Class Name
class MemInterface():

    #Base Constructor
    def __init__(self):

        #We want type for every Minimum VarTable type we can count on
        self.global_memory = MemManager('Global', 10000, 6000)
        self.local_memory = MemManager('Local', 16000, 6000)
        self.temporary_memory = MemManager('Temporary', 22000, 6000)
        self.constant_memory = MemManager('Constant', 28000, 6000)

    #Stores the value that is provided (defaulted to None by type) and returns memory allocation
    def global_memory_assign(self, v_type, value = None):
        return self.global_memory.obtain_address(v_type, value)

    def local_memory_assign(self, v_type, value = None):
        return self.local_memory.obtain_address(v_type, value)

    def constant_memory_assign(self, v_type, value = None):
        return self.constant_memory.obtain_address(v_type, value)

    def temporary_memory_assign(self, v_type, value = None):
        return self.temporary_memory.obtain_address(v_type, value)

    #Stores the value that is provided (defaulted to None by type) and returns memory allocation
    #No constant arrays or temporary arrays either.
    def sequential_global_assign(self, v_type, num_addresses, value = None):
        return self.global_memory.obtain_sequential_addresses(v_type, num_addresses, value)

    def sequential_local_assign(self, v_type, num_addresses, value = None):
        return self.local_memory.obtain_sequential_addresses(v_type, num_addresses, value)

    #Uses the defined limits (initial and final addresses) from MemManager to determine memory type
    def type_of_memory(self, address):
        if (address >= self.global_memory.initial and address <= self.global_memory.final):
            return 'global'
        elif (address >= self.local_memory.initial and address <= self.local_memory.final):
            return 'local'
        elif (address >= self.temporary_memory.initial and address <= self.temporary_memory.final):
            return 'temporary'
        elif (address >= self.constant_memory.initial and address <= self.constant_memory.final):
            return 'constant'
        else:
            print("Address " + str(address) + " is not within defined usable range.")
            sys.exit()

    #Using the corresponding type of memory, calls the function to return the content within the address
    def get_content(self, address):
        type_of_memory = self.type_of_memory(address)
        if type_of_memory == 'global':
            return self.global_memory.recover_content(address)
        elif type_of_memory == 'local':
            return self.local_memory.recover_content(address)
        elif type_of_memory == 'constant':
            return self.constant_memory.recover_content(address)
        elif type_of_memory == 'temporary':
            return self.temporary_memory.recover_content(address)


    #Using the corresponding type of memory, calls the function to change the content within the address
    def edit_memory_content(self, address, content):
        memory_type = self.type_of_memory(address)
        if memory_type == 'global':
            self.global_memory.modify_value(address, content)
        elif memory_type == 'local':
            self.local_memory.modify_value(address, content)
        elif memory_type == 'temporary':
            self.temporary_memory.modify_value(address, content)
        elif memory_type == 'constant':
            self.constant_memory.modify_value(address, content)

    #Check if a value is within the constant variable table memory space
    def constant_exists(self, v_type, value):
        return self.constant_memory.check_existing_value(v_type, value)

    #Function to clear memory slots for re-use
    #Local memory is considered temporary here because we want to be able to clear module memory after
    #we are done using it.
    def clear_temporary_memory(self):
        self.local_memory.reset_memory()
        self.temporary_memory.reset_memory()