"""
This module contains opcode functions and helper functions needed
"""

def one(memory, pointer, param_modes):
	"""
	Addition
	"""
	a, b = get_first_two_params(memory, pointer, param_modes)
	memory[memory[pointer+3]] = a + b
	pointer += 4
	return memory, pointer

def two(memory, pointer, param_modes):
	"""
	Multiplication
	"""
	a, b = get_first_two_params(memory, pointer, param_modes)
	memory[memory[pointer+3]] = a * b
	pointer += 4
	return memory, pointer

def three(memory, pointer, user_input):
	"""
	Saves user input to a given address. Does not use parameter modes
	because the only parameter is the address the user input is saved to
	"""
	if not user_input:
		user_input = input('Please input a value. ')

	memory[memory[pointer + 1]] = int(user_input)
	pointer += 2
	return memory, pointer

def four(memory, pointer, param_modes):
	"""
	Outputing value in memory
	"""
	output = memory[memory[pointer + 1]] if param_modes[0] == 0 else memory[pointer + 1]
	print(output)
	pointer += 2
	return output

def get_first_two_params(memory, pointer, param_modes):
	"""
	Returns the values to be used according to the parameter modes provided
	(helper function)
	"""
	a = memory[memory[pointer + 1]] if param_modes[0] == 0 else memory[pointer + 1]
	b = memory[memory[pointer + 2]] if param_modes[1] == 0 else memory[pointer + 2]
	return a, b
