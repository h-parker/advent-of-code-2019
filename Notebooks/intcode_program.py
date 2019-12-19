# takes in instructions and outputs the opcode and paramater modes of the instruction
def interpret_instructions(instruction):
	instruc_len = len(str(instruction))
	
	# take care of single digit instructions
	if instruc_len == 1:
		opcode = instruction
		if opcode == 3 or opcode == 4:
			param_modes = [0]
		elif opcode in [1, 2, 5, 6, 7, 8]:
			param_modes = [0,0]
		return opcode, param_modes
	
	opcode = int(str(instruction)[instruc_len-2: instruc_len])
	param_modes = [int(mode) for mode in str(instruction)[:instruc_len-2]]
	
	# reads instructions left to right, when they're written right to left
	# so we have to reverse the list
	param_modes.reverse()
	
	# take care of leading zeroes
	if (opcode in [1, 2, 5, 6, 7, 8]) and instruc_len < 5:
			param_modes.extend(0 for i in range(0, 5 - instruc_len))
	
	elif opcode == 4:
		if instruc_len == 2:
			param_modes.append(0)

	
	return opcode, param_modes


# runs the actual program
def intcode(sequence, inpt=False):
	temp = sequence.copy() # don't want to alter the input - work w/ a copy instead
	idx = 0
	opcode, param_modes = interpret_instructions(temp[0])
	while opcode != 99 and idx < len(temp):
		# perform operation & replacement
		if opcode == 3 and inpt:
			temp, idx = switch_case(opcode, temp, idx, param_modes, inpt[0])
			inpt.pop(0) # remove last input used

		else:
			temp, idx = switch_case(opcode, temp, idx, param_modes)
		
		# replace the opcode & param_modes
		opcode, param_modes = interpret_instructions(temp[idx])

	return temp


# makes switch-case for Python woohoo 
def switch_case(opcode, temp, idx, param_modes, inpt=False):
	# we use lambdas so that python lazily evaluates these 
	# functions -- a function will only be evaluated when
	# called in the return statement
	opcode_dict = {
		1: (lambda: opcode_1(temp, idx, param_modes)),
		2: (lambda: opcode_2(temp, idx, param_modes)),
		3: (lambda: opcode_3(temp, idx, param_modes, inpt)),
		4: (lambda: opcode_4(temp, idx, param_modes)),
		5: (lambda: opcode_5(temp, idx, param_modes)),
		6: (lambda: opcode_6(temp, idx, param_modes)),
		7: (lambda: opcode_7(temp, idx, param_modes)),
		8: (lambda: opcode_8(temp, idx, param_modes))
	}
	return opcode_dict.get(opcode, ('invalid ', 'invalid'))()

def get_first_two_params(temp, param_modes, idx):
	a = temp[temp[idx + 1]] if param_modes[0] == 0 else temp[idx + 1]
	b = temp[temp[idx + 2]] if param_modes[1] == 0 else temp[idx + 2]
	return a, b

def opcode_1(temp, idx, param_modes):
	a, b = get_first_two_params(temp, param_modes, idx)
	temp[temp[idx+3]] = a + b
	idx += 4
	return temp, idx

def opcode_2(temp, idx, param_modes):
	a, b = get_first_two_params(temp, param_modes, idx)
	temp[temp[idx+3]] = a * b
	idx += 4
	return temp, idx

def opcode_3(temp, idx, param_modes, inpt=False):
	if not inpt and inpt != 0: # not 0 == True -- avoid this!
		user_input = input("Enter your input. ")
		temp[temp[idx+1]] = int(user_input)
	else:
		temp[temp[idx+1]] = inpt
	idx += 2
	return temp, idx

def opcode_4(temp, idx, param_modes):
	print(temp[temp[idx+1]] if param_modes[0] == 0 else temp[idx+1])
	idx += 2
	return temp, idx

def opcode_5(temp, idx, param_modes):
	a, b = get_first_two_params(temp, param_modes, idx)
	if a != 0:
		idx = b
	else:
		idx += 3
	return temp, idx

def opcode_6(temp, idx, param_modes):
	a, b = get_first_two_params(temp, param_modes, idx)
	if a == 0:
		idx = b
	else:
		idx += 3
	return temp, idx

def opcode_7(temp, idx, param_modes):
	a, b = get_first_two_params(temp, param_modes, idx)
	if a < b:
		temp[temp[idx+3]] = 1
	else:
		temp[temp[idx+3]] = 0
	idx += 4
	return temp, idx

def opcode_8(temp, idx, param_modes):
	a, b = get_first_two_params(temp, param_modes, idx)
	if a == b:
		temp[temp[idx+3]] = 1
	else:
		temp[temp[idx+3]] = 0
	idx += 4
	return temp, idx