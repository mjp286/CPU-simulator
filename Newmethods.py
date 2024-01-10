data_file = "data_input.txt"
instruction_input = "instruction_input.txt"

class MIPS_Simulator:
    def __init__(self):
        self.registers = [0] * 32  # 32 general-purpose registers
        self.memory = [0] * 128  # 128 words of memory
        self.cpu = 0  # program counter
       

        with open(data_file, 'r') as file:
            for line in file:
                key, value = line.strip().split(',')
                address = int(key, 2)
                self.memory[address] = int(value)

    def CACHE(self, code, address):
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
            self.memory[address] = operands[1]
            self.cache.write_cache(address, operands[1])
            print(f"Write to memory and cache: address {address}, value {operands[1]}")
        else:
            print("Unknown CACHE operation")

    def ADD(self, Rd, Rs, Rt):
        self.registers[Rd] = self.registers[Rs] + self.registers[Rt]

    def ADDI(self, Rt, Rs, immd):
        self.registers[Rt] = self.registers[Rs] + immd

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

    def CACHE(self, code, address):
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
            self.memory[address] = operands[1]
            self.cache.write_cache(address, operands[1])
            print(f"Write to memory and cache: address {address}, value {operands[1]}")
        else:
            print("Unknown CACHE operation")

    def HALT(self):
        # Terminate Execution
        print("Execution halted.")
        exit()

    def execute_instruction(self, instruction, *operands):
        if instruction in ["ADD", "SUB", "SLT"]:
            # R-type instruction
            self.execute_r_type(instruction, *operands)
        elif instruction in ["ADDI", "LW", "SW"]:
            # I-type instruction
            self.execute_i_type(instruction, *operands)
        elif instruction in ["J", "JAL"]:
            # J-type instruction
            self.execute_j_type(instruction, *operands)
        else:
            print(f"Unknown instruction: {instruction}")

    def execute_r_type(self, instruction, rd, rs, rt):
        if instruction == "ADD":
            self.registers[rd] = self.registers[rs] + self.registers[rt]
        elif instruction == "SUB":
            self.registers[rd] = self.registers[rs] - self.registers[rt]
        elif instruction == "SLT":
            self.registers[rd] = 1 if self.registers[rs] < self.registers[rt] else 0

    def execute_i_type(self, instruction, rt, rs, immd):
        if instruction == "ADDI":
            self.registers[rt] = self.registers[rs] + immd
        elif instruction == "LW":
            address = self.registers[rs] + immd
            self.registers[rt] = self.CACHE("READ", address)
        elif instruction == "SW":
            address = self.registers[rs] + immd
            self.CACHE("WRITE", address, self.registers[rt])

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
                self.execute_instruction(opcode, *operands)

    def __str__(self):
        return f"Welcome to mjp286s MIPS simulator!\n registers={self.registers}\n memory={self.memory}\n program counter={self.cpu}"

# Example usage
simulator = MIPS_Simulator()
# simulator.ADD(1, 2, 3)
# print(simulator.registers)

# print(simulator.ADD(1,2,3))
print(simulator)