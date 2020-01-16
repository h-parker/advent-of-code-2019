import opcodes

class Intcode:
	"""
	Creating an instance of the Intcode class will create a computer that can be used to 
	read and execute Intcode programs. 
	"""
	def __init__(self, program, name='default', pointer = 0, user_input = False, 
				replacements = False):
		"""
		- program is the sequence of integers containing opcodes the integers they operate 
		on.
		- name is mostly here for debugging purposes
		- pointer is the address in memory the Intcode computer is currently operating on; 
		defaults to 0, since a new instance of an intcode computer will start at the 
		beginning
		- user_input is provided when you want to automate testing with user input
		- replacements should be a list of tuples, with the first position in each tuple 
		being the address in memory that should be replaced, and the second position in
		the tuple being the replacement value. For example, [(0, 3), (10, 33)] would result
		in the value in address 0 being replaced with 3 and the value in address 10 being
		replaced with 33 in whatever the program is. 
		"""
		self.memory = program.copy() # set initial memory 
		# extend the length of the memory to 100 times the size of the program
		self.memory.extend([0 for x in range(len(program)*100)]) 
		self.name = name
		self.pointer = pointer
		self.user_input = user_input
		self.replacements = replacements 
		self.relative_base = 0 # relative base for opcode 9
		self.halted = False # True once opcode 99 is reached
		self.curr_output = False # store last output from opcode 4
		self.paused = False # pause to wait to get input

		# False if you want to have the computer wait to recieve human input and True
		# if you are giving the computer input and it's operating on it's own, going
		# through the input supplied (or waiting for another computer to supply input)
		self.automate= bool(user_input)
		

	def intcode(self):
		"""
		Run the Intcode Computer on your program.
		"""
		# replace any values in the program as specified
		if self.replacements:
			for tup in self.replacements:
				self.memory[tup[0]] = tup[1]

		# get initial program 
		opcode, param_modes = self.__interpret_instructions__(self.memory[self.pointer])
		while not self.halted and not self.paused and self.pointer < len(self.memory):
			if opcode == 99:
				self.halted = True
			else:
				if opcode == 3:
					self.memory, self.pointer, self.paused = self.__execute_opcode__(opcode,
																	 param_modes)
					# get rid of last used input if there was input provided
					if not self.paused:
						self.user_input.pop(0)

				elif opcode == 9:
					self.memory, self.pointer, self.relative_base = self.__execute_opcode__(
																		opcode, param_modes)

				elif opcode != 4:
					self.memory, self.pointer = self.__execute_opcode__(opcode, param_modes)
				else:
					self.memory, self.pointer, self.curr_output = self.__execute_opcode__(
																			opcode, 
																			param_modes)

				opcode, param_modes = self.__interpret_instructions__(self.memory[self.pointer])

		return self.memory, self.curr_output



	def __interpret_instructions__(self, instruction):
		"""
		Private method to take in instructions and output the opcode and the parameter
		modes.
		"""
		instruc_len = len(str(instruction))
		opcode = int(str(instruction)[instruc_len - 2:])
		if opcode != 3:
			param_modes = [int(x) for x in str(instruction)[:instruc_len - 2]]

			# read from right to left, rather than left to right, so we have to reverse 
			# the order
			param_modes.reverse()

			if len(param_modes) < 2:
				if opcode != 4: # since opcode 4 only needs 1 parameter mode
					param_modes.extend([0 for x in range(2 - len(param_modes))])
				else:
					param_modes.extend([0 for x in range(1 - len(param_modes))])
		else:
			param_modes = []

		return opcode, param_modes


	# makes switch-case for Python woohoo 
	def __execute_opcode__(self, opcode, param_modes):
		"""
		Private method that executes the appropriate opcode function from the opcode
		module. 
		"""
		# we use lambdas so that python lazily evaluates these functions -- a function will 
		# only be evaluated when called in the return statement
		# print('computer', self.name, 'opcode:', opcode)
		# print('computer', self.name, 'pointer', self.pointer)
		# print('computer', self.name, 'memory:', self.memory)
		# print('computer', self.name, 'parameter modes:', param_modes)
		opcode_dict = {
			1: (lambda: opcodes.one(self.memory, self.pointer, param_modes,
				self.relative_base)),
			2: (lambda: opcodes.two(self.memory, self.pointer, param_modes,
				self.relative_base)),
			3: (lambda: opcodes.three(self.memory, self.pointer, self.user_input, 
				self.automate, self.paused)),
			4: (lambda: opcodes.four(self.memory, self.pointer, param_modes,
				self.relative_base)),
			5: (lambda: opcodes.five(self.memory, self.pointer, param_modes,
				self.relative_base)),
			6: (lambda: opcodes.six(self.memory, self.pointer, param_modes,
				self.relative_base)),
			7: (lambda: opcodes.seven(self.memory, self.pointer, param_modes,
				self.relative_base)),
			8: (lambda: opcodes.eight(self.memory, self.pointer, param_modes,
				self.relative_base)),
			9: (lambda: opcodes.nine(self.memory, self.pointer, param_modes,
				 self.relative_base))
		}
		return opcode_dict.get(opcode, (None, None))()


