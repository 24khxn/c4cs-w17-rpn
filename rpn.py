#!/usr/bin/env python3

import operator
	
OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	
}

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
			result = calculate(inpu)
			print("Result: ", result)
		except:
			print "Malformed input, try again"

if __name__ == '__main__':
	main()
