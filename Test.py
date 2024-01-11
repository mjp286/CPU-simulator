
from Newmethods import MIPS_Simulator
from Cache import Cache

def run_simulation():
    data_file = "data_input.txt"
    input_file = "instruction_input.txt"

    # Example usage
    simulator = MIPS_Simulator()
    print(simulator)

    # Test the program with instructions from instruction_input.txt
    simulator.test(input_file)

if __name__ == "__main__":
    run_simulation()