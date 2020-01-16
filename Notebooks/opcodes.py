"""
This module contains opcode functions and helper functions needed
"""

def one(memory, pointer, param_modes):
	"""
	Addition
	"""
	param = get_params(memory, pointer, param_modes, relative_base)
	memory[memory[pointer + 3]] = param[0] + param[1]
	pointer += 4
	return memory, pointer

def two(memory, pointer, param_modes):
	"""
	Multiplication
	"""
	param = get_params(memory, pointer, param_modes, relative_base)
	memory[memory[pointer + 3]] = param[0] * param[1]
	pointer += 4
	return memory, pointer

def three(memory, pointer, user_input, automate, paused):
	"""
	Saves user input to a given address. Does not use parameter modes
	because the only parameter is the address the user input is saved to
	"""
	if automate and not user_input:
		paused = True
		# return here so that the computer starts up again where it left off
		# once no longer paused
		return memory, pointer, paused

	elif not user_input:
		user_input = [int(input('Please input a value. '))]

	memory[memory[pointer + 1]] = user_input[0]
	pointer += 2

	return memory, pointer, paused

def four(memory, pointer, param_modes):
	"""
	Outputing value in memory
	"""
	param = get_params(memory, pointer, param_modes, relative_base)
	output = param[0]
	print(output)
	pointer += 2
	return memory, pointer, output

def five(memory, pointer, param_modes):
	param = get_params(memory, pointer, param_modes, relative_base)
	if param[0] != 0:
		pointer = param[1]
	else:
		pointer += 3
	return memory, pointer

def six(memory, pointer, param_modes):
	param = get_params(memory, pointer, param_modes, relative_base)
	if param[0] == 0:
		pointer = param[1]
	else:
		pointer += 3
	return memory, pointer

def seven(memory, pointer, param_modes):
	param = get_params(memory, pointer, param_modes, relative_base)
	if param[0] < param[1]:
		memory[memory[pointer + 3]] = 1
	else:
		memory[memory[pointer + 3]] = 0
	pointer += 4
	return memory, pointer

def eight(memory, pointer, param_modes):
	param = get_params(memory, pointer, param_modes, relative_base)
	if param[0] == param[1]:
		memory[memory[pointer + 3]] = 1
	else:
		memory[memory[pointer + 3]] = 0
	pointer += 4
	return memory, pointer

def nine(memory, pointer, param_modes, relative_base):
	param = get_params(memory, pointer, param_modes, relative_base)
	relative_base += param[0]
	pointer += 2
	return memory, pointer, relative_base


def get_params(memory, pointer, param_modes, relative_base):
	"""
	Returns the values to be used according to the parameter modes provided
	(helper function)
	"""
	parameters = []
	i = 1
	for mode in param_modes:
		if mode == 0:
			parameters.append(memory[memory[pointer + i]])
		elif mode == 1:
			parameters.append(memory[pointer + i])
		elif mode == 2:
			parameters.append(memory[memory[pointer+i] 
										+ relative_base])
		i += 1
	return parameters
