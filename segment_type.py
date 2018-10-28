import json
import sys

class TypeSegment():

    def __init__(self, segment_name, initial_address, final_address):
        self.name = segment_name
        self.initial_address = initial_address
        self.final_address = final_address
        self.current_address = initial_address
        self.segment = {}

    def __str__(self):
        return ("MemorySegment : " + self.name + "\n" +
                "   Initial allocated address: " + str(self.initial_address) + "\n" +
                "   Final allocated address: " + str(self.final_address) + "\n" +
                "   Current address: " + str(self.current_address) + "\n" +
                "   Addresses " + json.dumps(self.segment, indent=4))

    def space_availability(self, total_addresses=0):
        if self.current_address + total_addresses <= self.final_address:
            return True
        else:
            return False

    def valid_address(self, address):
        if address in self.segment:
            return True
        else:
            return False

    def obtain_address(self, value):
        if self.space_availability():
            address = self.current_address
            self.segment[address] = value
            self.current_address += 1
            return address
        else:
            print("There is no space available in the " + self.name + " memory segment.")
            sys.exit()

    def obtain_sequential_addresses(self, total_addresses, value):
        if self.available_space(total_addresses):
            base_address = self.current_address

            for i in range(total_addresses):
                self.segment[self.current_address] = value
                self.current_address += 1

            return base_address
        else:
            print("There is no space available in the " + self.name + " memory segment.")
            sys.exit()

    def get_value(self, address):
        if self.valid_address(address):
            return self.segment[address]
        else:
            print("The address type does not match the value type.")
            return None

    def check_existing_value(self, existing_value):
        for address, value in self.segment.items():
            if value == existing_value:
                return address
        return None

    def edit_value(self, address, value):
        if self.valid_address(address):
            self.segment[address] = value
        else:
            print("The change you wish to make to the value is not valid for the type of address.")
            sys.exit()

    def reset(self):
        self.segment.clear()
        self.current_address = self.initial_address