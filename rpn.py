#!/usr/bin/env python3

import operator, readline
from lazyme.string import color_print
	
OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	
}

def print_my_name_and_add_bullshit():
	vi = 4
	v = 3
	q = vi + v
	print("Sheehan")
	print("wow")
	print(vi + q)
	print(vi) 

def calculate(arg):
	stack = list()	
	for operand in arg.split():
		try: 
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
		
	return stack.pop()

def main():
	while True:
		try:
			inpu = input("rpn calc> ")
			if(inpu == 'e'):
				break
			result = calculate(inpu)
			if(result < 0):
				color_print(result, color='red')
			else:
				color_print(result, color='blue')
		except:
			print ("Malformed input, try again")

if __name__ == '__main__':
	main()
