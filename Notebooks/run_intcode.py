"""
Script to run Intcode
"""

from Intcode import Intcode

def main():

	program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

	ampA = Intcode(program=program, user_input=[4,0])
	mem, ampA_output = ampA.intcode()

	ampB = Intcode(program=program, user_input=[3, ampA_output])
	mem, ampB_output = ampB.intcode()

	ampC = Intcode(program=program, user_input=[2, ampB_output])
	mem, ampC_output = ampC.intcode()

	ampD = Intcode(program=program, user_input=[1, ampC_output])
	mem, ampD_output = ampD.intcode()

	ampE = Intcode(program=program, user_input=[0, ampD_output])
	mem, ampE_output = ampE.intcode()


if __name__ == "__main__":
    main()