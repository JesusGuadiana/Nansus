from segmented_memory import MemorySegment
import sys

class Memory():

    def __init__(self):
        self.global_memory = MemorySegment('Global', 10000, 3000)
        self.local_memory = MemorySegment('Local', 15000, 3000)
        self.constant_memory = MemorySegment('Constant', 25000, 3000)
        self.temp_memory = MemorySegment('temp', 30000, 3000)

    def obtain_global_address(self, value_type, value=None,):
        return self.global_memory.obtain_address(value_type, value)

    def obtain_local_address(self, value_type, value=None,):
        return self.local_memory.obtain_address(value_type, value)

    def obtain_constant_address(self, value_type, value=None):
        return self.constant_memory.obtain_address(value_type, value)

    def obtain_temp_address(self, value_type, value=None):
        return self.temp_memory.obtain_address(value_type, value)

    def determines_memory_type(self, address):
        if (address >= self.global_memory.initial_address and address <=
            self.global_memory.final_address):
            return 'global'
        elif (address >= self.local_memory.initial_address and address <=
            self.local_memory.final_address):
            return 'local'
        elif (address >= self.temp_memory.initial_address and address <=
            self.temp_memory.final_address):
            return 'temp'
        elif (address >= self.constant_memory.initial_address and address <=
            self.constant_memory.final_address):
            return 'constant'
        else:
            print("Invalid address: " + str(address))
            sys.exit()

    def get_value(self, address):
        memory_type = self.determines_memory_type(address)
        if memory_type == 'global':
            return self.global_memory.get_value(address)
        elif memory_type == 'local':
            return self.local_memory.get_value(address)
        elif memory_type == 'temp':
            return self.temp_memory.get_value(address)
        elif memory_type == 'constant':
            return self.constant_memory.get_value(address)

    def edit_value(self, address, value):
        memory_type = self.determines_memory_type(address)
        if memory_type == 'global':
            self.global_memory.edit_value(address, value)
        elif memory_type == 'local':
            self.local_memory.edit_value(address, value)
        elif memory_type == 'temp':
            self.temp_memory.edit_value(address, value)
        elif memory_type == 'constant':
            self.constant_memory.edit_value(address, value)

    def check_existing_constant_value(self, value_type, value):
        return self.constant_memory.check_existing_value(value_type, value)

    def reset_temp_memory(self):
        self.local_memory.reset_memory()
        self.temp_memory.reset_memory()

    def print_memory(self, memory_type, segment_type = ""):
        if memory_type == 'global':
            self.global_memory.print_segment(segment_type)
        elif memory_type == 'local':
            self.local_memory.print_segment(segment_type)
        elif memory_type == 'temp':
            self.temp_memory.print_segment(segment_type)
        elif memory_type == 'constant':
            self.constant_memory.print_segment(segment_type)
        else:
            self.global_memory.print_segment(segment_type)
            self.local_memory.print_segment(segment_type)
            self.temp_memory.print_segment(segment_type)
            self.constant_memory.print_segment(segment_type)