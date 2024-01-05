msg = "Hello World"
print(msg)

class MIPS_Simulator:
    def __init__(self):
        self.registers = [0] * 32  # 32 general-purpose registers
        self.memory = [0] * 1024  # 1024 words of memory
        self.PC = 0  # Program Counter

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
            self.PC = (self.PC + 4) + offset * 4

    def J(self, target):
        self.PC = target * 4

    def JAL(self, target):
        self.registers[7] = self.PC + 4
        self.PC = target * 4

    def LW(self, Rt, offset, Rs):
        address = self.registers[Rs] + offset
        self.registers[Rt] = self.memory[address]

    def SW(self, Rt, offset, Rs):
        address = self.registers[Rs] + offset
        self.memory[address] = self.registers[Rt]

    def CACHE(self, code):
        # Implement cache functionality based on the code
        pass

    def HALT(self):
        # Terminate Execution
        print("Execution halted.")
        exit()

    def execute_instruction(self, instruction, *operands):
        # Execute the specified instruction
        if hasattr(self, instruction):
            getattr(self, instruction)(*operands)
        else:
            print(f"Unknown instruction: {instruction}")

# Example usage
simulator = MIPS_Simulator()
simulator.ADD(1, 2, 3)
print(simulator.registers)
