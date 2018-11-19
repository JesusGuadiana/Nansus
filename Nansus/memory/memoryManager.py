# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language 
#  memoryManager.py
#  (Handles the logic of value storage and Memory Allocation)
#  Last edit: 18/11/2018
# -----------------------------------------------------------------------------
#Packages Imported
import sys

#Class Name
class MemManager():

    #Base constructor
    def __init__(self, identifier, initial, num_addresses):

        #Base attribute definitions for Memory Space
        self.identifier = identifier
        self.initial = initial
        self.final = initial + num_addresses - 1
        self.partition_size = int(num_addresses / 4) #This is 1500 memory spaces per type of value

        #Initial and final address for each of the three types of variable
        self.int_initial = initial #Base + 0
        self.int_final = initial + self.partition_size - 1 #Base + 1499
        self.char_initial = initial + self.partition_size #Base + 1500
        self.char_final = initial + self.partition_size * 2 - 1 #Base + 2999
        self.float_initial = initial + self.partition_size * 2 #Base + 3000
        self.float_final = initial + self.partition_size * 3 - 1 #Base + 4499
        self.bool_initial = initial + self.partition_size * 2 #Base + 4500
        self.bool_final = initial + self.partition_size * 3 - 1 #Base + 5999

        #Pointers to the current memory of each type
        self.int_current = self.int_initial
        self.char_current = self.char_initial
        self.float_current = self.float_initial
        self.bool_current = self.bool_initial

        #A subsegment dictionary in the form of a list for every utilized address type plus its value
        self.int_partition = {}
        self.char_partition = {}
        self.float_partition = {}
        self.bool_partition = {}

    #Verifies that the address being requested is available within its designated type memory range
    def available_address(self, part_type, extra_addresses_to_assign = 0):
        if part_type == 'int':
            if self.int_current + extra_addresses_to_assign <= self.int_final:
                return True
            else:
                return False
        elif part_type == 'float':
            if self.float_current + extra_addresses_to_assign <= self.float_final:
                return True
            else:
                return False
        elif part_type == 'char':
            if self.char_current + extra_addresses_to_assign <= self.char_final:
                return True
            else:
                return False
        elif part_type == 'bool':
            if self.bool_current + extra_addresses_to_assign <= self.bool_final:
                return True
            else:
                return False

    #Verifies that an address being used by getter or modifier exists before usage
    def valid_address(self, address):
        part_type = self.check_partition_type(address)
        if part_type == 'int':
            if address in self.int_partition:
                return True
            else:
                return False
        elif part_type == 'float':
            if address in self.float_partition:
                return True
            else:
                return False
        elif part_type == 'char':
            if address in self.char_partition:
                return True
            else:
                return False
        elif part_type == 'bool':
            if address in self.bool_partition:
                return True
            else:
                return False
        
    #Generates the address for a singular memory slot of specified type
    def obtain_address(self, part_type, value = None):
        if part_type == 'int':
            if value is None:
                value = 0
            if self.available_address(part_type):
                new_address = self.int_current
                self.int_partition[new_address] = value
                self.int_current += 1
                return new_address
            else:
                print("There is no remaining space in the " + part_type + " memory partition.")
                sys.exit()

        elif part_type == 'float':
            if value is None:
                value = 0.0
            if self.available_address(part_type):
                new_address = self.float_current
                self.float_partition[new_address] = value
                self.float_current += 1
                return new_address
            else:
                print("There is no remaining space in the " + part_type + " memory partition.")
                sys.exit()

        elif part_type == 'char':
            if value is None:
                value = ""
            if self.available_address(part_type):
                new_address = self.char_current
                self.char_partition[new_address] = value
                self.char_current += 1
                return new_address
            else:
                print("There is no remaining space in the " + part_type + " memory partition.")
                sys.exit()

        elif part_type == 'bool':
            if value is None:
                value = False
            if self.available_address(part_type):
                new_address = self.bool_current
                self.bool_partition[new_address] = value
                self.bool_current += 1
                return new_address
            else:
                print("There is no remaining space in the " + part_type + " memory partition.")
                sys.exit()

    #Generates the address for a multi-slot memory partition of specified type
    def obtain_sequential_addresses(self, part_type, addresses_to_assign, value=None):
        if part_type == 'int':
            if value is None:
                value = 0
            if self.available_address(part_type, addresses_to_assign - 1):
                base_address = self.int_current

                for i in range(addresses_to_assign):
                    self.int_partition[self.int_current] = value
                    self.int_current += 1

                return base_address
            else:
                print("There is no remaining space in the " + part_type + " memory partition.")
                sys.exit()

        elif part_type == 'float':
            if value is None:
                value = 0.0
            if self.available_address(part_type, extra_addresses_to_assign):
                base_address = self.float_current

                for i in range(addresses_to_assign):
                    self.float_partition[self.float_current] = value
                    self.float_current += 1

                return base_address
            else:
                print("There is no remaining space in the " + part_type + " memory partition.")
                sys.exit()

        elif part_type == 'char':
            if value is None:
                value = ""
            if self.available_address(part_type, extra_addresses_to_assign):
                base_address = self.char_current

                for i in range(addresses_to_assign):
                    self.char_partition[self.char_current] = value
                    self.char_current += 1

                return base_address
            else:
                print("There is no remaining space in the " + part_type + " memory partition.")
                sys.exit()

        elif part_type == 'bool':
            if value is None:
                value = ""
            if self.available_address(part_type, extra_addresses_to_assign):
                base_address = self.bool_current

                for i in range(addresses_to_assign):
                    self.bool_partition[self.bool_current] = value
                    self.bool_current += 1

                return base_address
            else:
                print("There is no remaining space in the " + part_type + " memory partition.")
                sys.exit()

    #Checks the type of partition that is being handled for a certain specified address
    def check_partition_type(self, address):
        if (address >= self.int_initial and address <= self.int_final):
            return 'int'
        elif (address >= self.float_initial and address <= self.float_final):
            return 'float'
        elif (address >= self.char_initial and address <= self.char_final):
            return 'char'
        elif (address >= self.bool_initial and address <= self.bool_final):
            return 'bool'
        else:
            print("Invalid address in the " + self.identifier + " memory")
            sys.exit()

    #Getter for the content within a memory address
    def recover_content(self, address):
        part_type = self.check_partition_type(address)
        if part_type == 'int':
            if self.valid_address(address):
                return self.int_partition[address]
            else:
                print("The address type does not match the value type.")
                return None
        elif part_type == 'float':
            if self.valid_address(address):
                return self.float_partition[address]
            else:
                print("The address type does not match the value type.")
                return None
        elif part_type == 'char':
            if self.valid_address(address):
                return self.char_partition[address]
            else:
                print("The address type does not match the value type.")
                return None
        elif part_type == 'bool':
            if self.valid_address(address):
                return self.bool_partition[address]
            else:
                print("The address type does not match the value type.")
                return None

    #Setter for the content within a memory address
    def modify_value(self, address, value):
        part_type = self.check_partition_type(address)
        if part_type == 'int':
            if self.valid_address(address):
                self.int_partition[address] = value
            else:
                print("The value entered for the modification is not compatible with the address type.")
                sys.exit()
        elif part_type == 'float':
            if self.valid_address(address):
                self.float_partition[address] = value
            else:
                print("The value entered for the modification is not compatible with the address type.")
                sys.exit()
        elif part_type == 'char':
            if self.valid_address(address):
                self.char_partition[address] = value
            else:
                print("The value entered for the modification is not compatible with the address type.")
                sys.exit()
        elif part_type == 'bool':
            if self.valid_address(address):
                self.bool_partition[address] = value
            else:
                print("The value entered for the modification is not compatible with the address type.")
                sys.exit()

    #Boolean verifier for existence of a value within the addresses of the same type
    def check_existing_value(self, part_type, e_value):

        if part_type == 'int':
            for address, value in self.int_partition.items():
                if value == e_value:
                    return address
                return None

        elif part_type == 'float':
            for address, value in self.float_partition.items():
                if value == e_value:
                    return address
                return None

        elif part_type == 'char':
            for address, value in self.char_partition.items():
                if value == e_value:
                    return address
                return None

        elif part_type == 'bool':
            for address, value in self.bool_partition.items():
                if value == e_value:
                    return address
                return None

    #Resets the memory usage to the default and clears the used up memory dictionaries
    def reset_memory(self):
        self.int_partition.clear()
        self.float_partition.clear()
        self.char_partition.clear()
        self.bool_partition.clear()
        self.int_current = self.int_initial
        self.float_current = self.float_current
        self.char_current = self.char_current
        self.bool_current = self.bool_current