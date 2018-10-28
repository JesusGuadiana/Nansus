from segment_type import TypeSegment
import sys

class MemorySegment():
    def __init__(self, memory_name, initial_address, total_addresses):
        self.name = memory_name
        self.type_segment_size = int(total_addresses / 3)
        self.initial_address = initial_address
        self.final_address= initial_address + total_addresses - 1

        self.int_initial_address = initial_address
        self.int_final_address = initial_address + self.type_segment_size - 1
        self.float_initial_address = initial_address + self.type_segment_size
        self.float_final_address = initial_address + self.type_segment_size * 2 - 1
        self.char_initial_address = initial_address + self.type_segment_size * 2
        self.char_final_address = initial_address + self.type_segment_size * 3 - 1

        self.int_segment = TypeSegment('Integer', self.int_initial_address,
            self.int_final_address)
        self.decimal_segment = TypeSegment('Decimal', self.decimal_initial_address,
            self.decimal_final_address)
        self.char_segment = TypeSegment('Char', self.char_initial_address,
            self.char_final_address)

    def obtain_address(self, segment_type, value=None):
        if segment_type == 'int':
            if value is None:
                value = 0
            return self.int_segment.obtain_address(value)
        elif segment_type == 'decimal':
            if value is None:
                value = 0.0
            return self.decimal_segment.obtain_address(value)
        elif segment_type == 'char':
            if value is None:
                value = ""
            return self.char_segment.obtain_address(value)

    def obtain_sequential_addresses(self, segment_type, total_addresses, value=None):
        if segment_type == 'int':
            if value is None:
                value = 0
            return self.int_segment.obtain_sequential_addresses(total_addresses, value)
        elif segment_type == 'decimal':
            if value is None:
                value = 0.0
            return self.decimal_segment.obtain_sequential_addresses(total_addresses, value)
        elif segment_type == 'char':
            if value is None:
                value = ""
            return self.char_segment.obtain_sequential_addresses(total_addresses, value)

    def verify_segment_type(self, address):
        if (address >= self.int_initial_address and address <=
            self.int_final_address):
            return 'int'
        elif (address >= self.decimal_initial_address and address <=
            self.decimal_final_address):
            return 'decimal'
        elif (address >= self.char_initial_address and address <=
            self.char_final_address):
            return 'char'
        else:
            print("Invalid address in the " + self.name + " memory")
            sys.exit()

    def get_value(self, address):
        segment_type = self.verify_segment_type(address)
        if segment_type == 'int':
            return self.int_segment.get_value(address)
        elif segment_type == 'decimal':
            return self.decimal_segment.get_value(address)
        elif segment_type == 'char':
            return self.char_segment.get_value(address)

    def edit_value(self, address, value):
        segment_type = self.verify_segment_type(address)
        if segment_type == 'int':
            self.int_segment.edit_value(address, value)
        elif segment_type == 'decimal':
            self.decimal_segment.edit_value(address, value)
        elif segment_type == 'char':
            self.char_segment.edit_value(address, value)

    def check_existing_value(self, segment_type, value):
        if segment_type == 'int':
            return self.int_segment.check_existing_value(value)
        elif segment_type == 'decimal':
            return self.decimal_segment.check_existing_value(value)
        elif segment_type == 'char':
            return self.char_segment.check_existing_value(value)

    def reset_memory(self):
        self.int_segment.reset()
        self.decimal_segment.reset()
        self.bool_segment.reset()
        self.char_segment.reset()

    def print_segment(self, segment_type = ""):
        print("Memory-Space : " + self.name + "\n" +
              "   Initial allocated address : " + str(self.initial_address) + "\n" +
              "   Final allocated address : " + str(self.final_address))
        if segment_type == 'int':
            print(self.int_segment)
        elif segment_type == 'decimal':
            print(self.decimal_segment)
        elif segment_type == 'char':
            print(self.char_segment)
        else:
            print(self.int_segment)
            print(self.decimal_segment)
            print(self.char_segment)