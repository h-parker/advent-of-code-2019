"""
Script to run Intcode
"""

from Intcode import Intcode
from itertools import permutations


def main():

	program = [3,8,1001,8,10,8,105,1,0,0,21,34,59,76,101,114,195,276,357,438,99999,3,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,3,9,102,2,9,9,4,9,99,3,9,101,4,9,9,102,5,9,9,101,5,9,9,4,9,99,3,9,102,2,9,9,1001,9,4,9,102,4,9,9,1001,9,4,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]
	max_signal = 0

	for phase in list(permutations(range(5, 10), 5)):

		amps = [Intcode(name='A', program=program, user_input=[phase[0]]),
				Intcode(name='B', program=program, user_input = [phase[1]]),
				Intcode(name='C', program=program, user_input = [phase[2]]),
				Intcode(name='D', program=program, user_input = [phase[3]]),
				Intcode(name='E', program=program, user_input = [phase[4]])]

		curr_amp = 0
		next_input = 0 # Amp A is given 0 as its first input (besides its phase)

		while not all(amp.halted for amp in amps):
			# each amp can be unpaused since there's output from the last amp
			# that it can use to continue running
			amps[curr_amp].paused = False
			amps[curr_amp].user_input.append(next_input)
			mem, next_input = amps[curr_amp].intcode()
			curr_amp  = (curr_amp + 1) % 5 # keep cycling through all 5 amps running

		if max_signal < next_input:
			max_signal = next_input 

	print('max is', max_signal)



	# max_signal = 0

	# for perm in list(permutations(range(5), 5)):
	# 	result = 0
	# 	ampA = Intcode(program=program, user_input=[perm[0],0])
	# 	mem, ampA_output = ampA.intcode()

	# 	ampB = Intcode(program=program, user_input=[perm[1], ampA_output])
	# 	mem, ampB_output = ampB.intcode()

	# 	ampC = Intcode(program=program, user_input=[perm[2], ampB_output])
	# 	mem, ampC_output = ampC.intcode()

	# 	ampD = Intcode(program=program, user_input=[perm[3], ampC_output])
	# 	mem, ampD_output = ampD.intcode()

	# 	ampE = Intcode(program=program, user_input=[perm[4], ampD_output])
	# 	mem, ampE_output = ampE.intcode()


	# 	if ampE_output > max_signal:
	# 		max_signal = ampE_output


	# print('max signal is', max_signal)

if __name__ == "__main__":
	main()