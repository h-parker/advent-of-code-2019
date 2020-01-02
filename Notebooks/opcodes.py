def one(program, idx, param_modes):
	a, b = get_first_two_params(program, param_modes, idx)
	program[program[idx+3]] = a + b
	idx += 4
	return program, idx

def two(program, idx, param_modes):
	a, b = get_first_two_params(program, param_modes, idx)
	program[program[idx+3]] = a * b
	idx += 4
	return program, idx

def get_first_two_params(program, param_modes, idx):
	a = program[program[idx + 1]] if param_modes[0] == 0 else program[idx + 1]
	b = program[program[idx + 2]] if param_modes[1] == 0 else program[idx + 2]
	return a, b
