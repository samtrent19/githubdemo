# Mark: The basic operations of our calculator
def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mul(a, b):
	return a * b

def div(a, b):
	return a / b

def mod(a, b):
	return a % b

#Mark: Our main method which will run when we call the application
#I'm adding a comment just to test what it will do
def main():
	a = 66	#First number
	b = 33	#Second number
	result = div(a,b)	# First divided by second
	print("The result is %.2f" % result)

if __name__ == "__main__":
	main()
