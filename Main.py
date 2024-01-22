
from MIPS_Simulator import MIPS_Simulator
from Cache import Cache

def run_simulation():
    input_file = "instruction_input.txt"

    # Testing the simulator 
    simulator = MIPS_Simulator()
    print(simulator)

    # Run the program with instructions from instruction_input.txt
    simulator.run(input_file)
   


if __name__ == "__main__":
    run_simulation()