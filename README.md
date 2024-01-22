# CPU simulator
 Computer Architecture Project for Codecademy

The goal of this project is to create a program that simulates the functionalities of a CPU.  My program implements an Instruction Set Architecture that processes MIPS Instructions.  A data_input.txt file is provided to populate the memory and an instruction_input.txt file is provided to test the functionality.  I added additional instructions to the instruction_input file to test all of the instructions the MIPS Simulator can process.

The program can be run by using Main.py. Different instructions can be added to the instruction_input.txt file or another '.txt' file can be used. If a different '.txt' file is used, the name of the file needs to be updated in Main.py. The MIPS Simulator can be populated with different data by altering the data_input file in MIPS_Simulator.py. The output of the program prints the state of the MIPS_Simulator(registers, memory, program counter) before the instruction is run and after the instruction is run. The output prints the state of the Cache after a "Cache" instruction is run.