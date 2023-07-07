# Python program showing
# use of __call__() method

class MyDecorator:
	def __init__(self, function):
		self.function = function
	
	def __call__(self):
		print("hi")
		self.function()
		print("hi")


# adding class decorator to the function
@MyDecorator
def function():
	print("GeeksforGeeks")

function()
