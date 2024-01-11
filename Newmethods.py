data_file = "data_input.txt"
input_file = "instruction_input.txt"

from Cache import Cache


class MIPS_Simulator:
    def __init__(self):
        self.registers = [0] * 32  # 32 general-purpose registers
        self.memory = [0] * 128  # 128 words of memory
        self.cpu = 0  # program counter
        self.cache = Cache()
       

        with open(data_file, 'r') as file:
            for line in file:
                key, value = line.strip().split(',')
                address = int(key, 2)
                self.memory[address] = int(value)


    def ADD(self, Rd, Rs, Rt):
        self.registers[Rd] = self.registers[Rs] + self.registers[Rt]

    def ADDI(self, Rt, Rs, immd):
        self.registers[Rt] = self.registers[Rs] + int(immd)

    def SUB(self, Rd, Rs, Rt):
        self.registers[Rd] = self.registers[Rs] - self.registers[Rt]

    def SLT(self, Rd, Rs, Rt):
        self.registers[Rd] = 1 if self.registers[Rs] < self.registers[Rt] else 0

    def BNE(self, Rs, Rt, offset):
        if self.registers[Rs] != self.registers[Rt]:
            self.cpu = (self.cpu + 4) + offset * 4

    def J(self, target):
        self.cpu = target * 4

    def JAL(self, target):
        self.registers[7] = self.cpu + 4
        self.cpu = target * 4

    def LW(self, Rt, offset, Rs):
        address = self.registers[Rs] + offset
        self.registers[Rt] = self.memory[address]

    def SW(self, Rt, offset, Rs):
        address = self.registers[Rs] + offset
        self.memory[address] = self.registers[Rt]

    def CACHE(self, code, address, value = None):
        if code == "READ":
            result = self.cache.search_cache(address)
            if result is not None:
                print(f"Cache hit for address {address}")
                return result
            else:
                print(f"Cache miss for address {address}")
                result_from_memory = self.memory[address]
                self.cache.write_cache(address, result_from_memory)
                return result_from_memory
        elif code == "WRITE":
            # Assuming operands contain address and value for write operation
            self.memory[address] = value
            self.cache.write_cache(address, value)
            print(f"Write to memory and cache: address {address}, value {value}")
        else:
            print("Unknown CACHE operation")

    def HALT(self):
        # Terminate Execution
        print("Execution halted.")
        exit()

    def execute_instruction(self, opcode, *operands):
        if opcode == "CACHE":
            # Special handling for CACHE instruction
            self.execute_cache_instruction(*operands)
        elif opcode in ["ADD", "SUB", "SLT"]:
            # R-type instruction
            self.execute_r_type(opcode, *operands)
        elif opcode in ["ADDI", "LW", "SW"]:
            # I-type instruction
            self.execute_i_type(opcode, *operands)
        elif opcode in ["J", "JAL"]:
            # J-type instruction
            self.execute_j_type(opcode, *operands)
        elif opcode == "HALT":
            self.HALT()
        else:
            print(f"Unknown instruction: {opcode}")

    def execute_cache_instruction(self, address):
        address = int(address)
        result = self.CACHE("READ", address)
        print(f"Result from CACHE READ: {result}")

    def execute_r_type(self, instruction, rd, rs, rt):
        try:
            self.registers[rd] = self.registers[rs] + self.registers[rt]
        except IndexError:
            print(f"Error accessing registers. Instruction: {instruction} {rd}, {rs}, {rt}")

    def execute_i_type(self, instruction, rt, rs, immd):
        immd = int(immd)
        rt = int(rt)
        rs = int(rs)

        if instruction == "ADDI":
            try:
                self.registers[rt] = self.registers[rs] + int(immd)
            except IndexError:
                 print(f"Error accessing registers. Instruction: {instruction} {rt}, {rs}, {immd}")
        elif instruction == "LW":
            address = self.registers[rs] + immd
            data = self.CACHE("READ", address)
            self.registers[rt] = data
        elif instruction == "SW":
             address = self.registers[rs] + immd
             self.CACHE("WRITE", address, self.registers[rt])
        else:
             print(f"Unknown I-type instruction: {instruction}")
  
    def execute_j_type(self, instruction, target):
        if instruction == "J":
            self.cpu = target * 4
        elif instruction == "JAL":
            self.registers[7] = self.cpu + 4
            self.cpu = target * 4

    def test(self, input_file):
        with open(input_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                opcode = parts[0]
                operands = parts[1:]

                if opcode == "CACHE":
                    # Special handling for CACHE instruction with a single operand
                    operands = [int(operands[0])]  # Convert the operand to an integer
                else:
                    # Convert register names to integers for other instructions
                    operands = [int(operand[1:]) if operand.startswith('R') else operand for operand in operands]

                self.execute_instruction(opcode, *operands)

    def __str__(self):
        return f"MIPS Simulator:\n registers={self.registers}\n memory={self.memory}\n program counter={self.cpu}"
    
# # Example usage
# simulator = MIPS_Simulator()
# print(simulator)
# simulator.test(input_file)

