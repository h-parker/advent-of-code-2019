"""
This module contains opcode functions and helper functions needed
"""

def one(memory, pointer, param_modes, relative_base, debug):
	"""
	Addition
	"""
	param = get_params(memory, pointer, param_modes, relative_base)
	memory[param[2]] = memory[param[0]] + memory[param[1]]

	if debug:
		print('parameters are', [memory[x] for x in param])
		print('memory loc', param[2])
		print('memory loc', param[2], 'changed to', memory[param[2]])
		print('-----------------')
	
	pointer += 4

	return memory, pointer




def two(memory, pointer, param_modes, relative_base, debug):
	"""
	Multiplication
	"""
	param = get_params(memory, pointer, param_modes, relative_base)
	memory[param[2]] = memory[param[0]] * memory[param[1]]

	if debug:
		print('parameters are', [memory[x] for x in param])
		print('memory loc', param[2])
		print('memory loc', param[2], 'changed to', memory[param[2]])
		print('-----------------')
	
	
	pointer += 4
	
	return memory, pointer




def three(memory, pointer, user_input, param_modes, automate, paused, 
	relative_base, debug):
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

	param = get_params(memory, pointer, param_modes, relative_base)

	memory[param[0]] = user_input[0]
	if debug:
		print('memory at loc', param[0],
				'changed to', memory[param[0]])
		print('-----------------')

	
	pointer += 2

	return memory, pointer, paused, user_input




def four(memory, pointer, param_modes, relative_base):
	"""
	Outputing value in memory
	"""
	param = get_params(memory, pointer, param_modes, relative_base)
	output = memory[param[0]]
	print(output)
	pointer += 2

	return memory, pointer, output




def five(memory, pointer, param_modes, relative_base, debug):
	param = get_params(memory, pointer, param_modes, relative_base)
	if memory[param[0]] != 0:
		pointer = memory[param[1]]
	else:
		pointer += 3

	if debug:
		print('parameters are', [memory[x] for x in param])
		print('pointer is now', pointer)
		print('-----------------')

	return memory, pointer




def six(memory, pointer, param_modes, relative_base, debug):
	param = get_params(memory, pointer, param_modes, relative_base)
	if memory[param[0]] == 0:
		pointer = memory[param[1]]
	else:
		pointer += 3

	if debug:
		print('parameters are', [memory[x] for x in param])
		print('pointer is now', pointer)
		print('-----------------')

	return memory, pointer




def seven(memory, pointer, param_modes, relative_base, debug):
	param = get_params(memory, pointer, param_modes, relative_base)
	
	if memory[param[0]] < memory[param[1]]:
		memory[param[2]] = 1
	else:
		memory[param[2]] = 0

	pointer += 4

	if debug:
		print('parameters are', [memory[x] for x in param])
		print('memory loc', param[2])
		print('memory changed to', memory[param[2]])
		print('-----------------')

	return memory, pointer




def eight(memory, pointer, param_modes, relative_base, debug):
	param = get_params(memory, pointer, param_modes, relative_base)
	
	if memory[param[0]] == memory[param[1]]:
		memory[param[2]] = 1
	else:
		memory[param[2]] = 0
	pointer += 4

	if debug:
		print('parameters are', [memory[x] for x in param])
		print('memory loc', param[2])
		print('memory changed to', memory[param[2]])
		print('-----------------')

	return memory, pointer




def nine(memory, pointer, param_modes, relative_base, debug):
	param = get_params(memory, pointer, param_modes, relative_base)
	relative_base += memory[param[0]]
	pointer += 2

	if debug:
		print('parameters are', [memory[x] for x in param])
		print('relative base changed to', relative_base)
		print('-----------------')

	return memory, pointer, relative_base


def get_params(memory, pointer, param_modes, relative_base):
	"""
	Returns the memory location to be used according to the parameter modes 
	provided (helper function)
	"""
	parameters = []
	i = 1
	for mode in param_modes:
		if mode == 0:
			parameters.append(memory[pointer + i])
		elif mode == 1:
			parameters.append(pointer + i)
		elif mode == 2:
			
			parameters.append(memory[pointer+i] + relative_base)
		i += 1
	return parameters
