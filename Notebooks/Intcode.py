import opcodes

class Intcode:
	"""
	Creating an instance of the Intcode class will create a computer that can be used to read
	and execute Intcode programs. 
	"""
	def __init__(self, program, idx = 0, user_input = False, replacements = False):
		"""
		- program is the sequence of integers containing opcodes the integers they operate on.
		- idx is the position the Intcode computer is currently operating on; 
		defaults to 0, since a new instance of an intcode computer will start at the beginning
		- user_input is provided when you want to automate testing with user input
		- replacements should be a list of tuples, with the first position in each tuple 
		being the position of the program that should be replaced, and the second position in
		the tuple being the replacement value. For example, [(0, 3), (10, 33)] would result
		in the value in position 0 being replaced with 3 and the value in position 10 being
		replaced with 33 in whatever the program is. 
		"""
		self.program = program.copy() # don't want to alter the original program
		self.idx = idx
		self.user_input = user_input
		self.replacements = replacements
		self.halted = False # True once opcode 99 is reached
		self.curr_output = None # store last output from opcode 4

	def intcode(self):
		# replace any values in the program as specified
		if self.replacements:
			for tup in self.replacements:
				self.program[tup[0]] = tup[1]

		opcode, param_modes = self.__interpret_instructions__(self.program[self.idx])
		while not self.halted and self.idx < len(self.program):
			if opcode == 99:
				self.halted = True
			else:
				self.program, self.idx = self.__execute_opcode__(opcode, param_modes)
				opcode, param_modes = self.__interpret_instructions__(self.program[self.idx])

		return self.program



	def __interpret_instructions__(self, instruction):
		opcode = int(instruction)
		param_modes = [0,0]
		return opcode, param_modes


	# makes switch-case for Python woohoo 
	def __execute_opcode__(self, opcode, param_modes):
		# we use lambdas so that python lazily evaluates these functions -- a function will 
		# only be evaluated when called in the return statement
		opcode_dict = {
			1: (lambda: opcodes.one(self.program, self.idx, param_modes)),
			2: (lambda: opcodes.two(self.program, self.idx, param_modes)),
		}
		return opcode_dict.get(opcode, (None, None))()


