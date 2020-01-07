"""
This module contains opcode functions and helper functions needed
"""

def one(memory, pointer, param_modes):
	"""
	Addition
	"""
	param = get_params(memory, pointer, param_modes)
	memory[memory[pointer + 3]] = param[0] + param[1]
	pointer += 4
	return memory, pointer

def two(memory, pointer, param_modes):
	"""
	Multiplication
	"""
	param = get_params(memory, pointer, param_modes)
	memory[memory[pointer + 3]] = param[0] * param[1]
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
	param = get_params(memory, pointer, param_modes)
	output = param[0]
	print(output)
	pointer += 2
	return memory, pointer, output

def five(memory, pointer, param_modes):
	param = get_params(memory, pointer, param_modes)
	if param[0] != 0:
		pointer = param[1]
	else:
		pointer += 3
	return memory, pointer

def six(memory, pointer, param_modes):
	param = get_params(memory, pointer, param_modes)
	if param[0] == 0:
		pointer = param[1]
	else:
		pointer += 3
	return memory, pointer

def seven(memory, pointer, param_modes):
	param = get_params(memory, pointer, param_modes)
	if param[0] < param[1]:
		memory[memory[pointer + 3]] = 1
	else:
		memory[memory[pointer + 3]] = 0
	pointer += 4
	return memory, pointer

def eight(memory, pointer, param_modes):
	param = get_params(memory, pointer, param_modes)
	if param[0] == param[1]:
		memory[memory[pointer + 3]] = 1
	else:
		memory[memory[pointer + 3]] = 0
	pointer += 4
	return memory, pointer

def get_params(memory, pointer, param_modes):
	"""
	Returns the values to be used according to the parameter modes provided
	(helper function)
	"""
	parameters = []
	i = 1
	for mode in param_modes:
		parameters.append(memory[memory[pointer + i]] if param_modes[i - 1] == 0 else memory[pointer + i])
		i += 1
	return parameters
