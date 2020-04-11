from functools import wraps

def sample_decorator(target_function):
	print('hey')
	def wrapper(*args, **kwargs):
		print
		output = target_function(*args, **kwargs)
		return output
	return target_function

def sample_decorator_with_parameter(sample_param):
	def inner_function(target_function):
		@wraps(target_function)
		def wrapper(*args, **kwargs):
			print('before calling target function')
			output = target_function(*args, **kwargs)
			print('after calling target function')
			return output
		return wrapper
	return inner_function

@sample_decorator
def some_function():
	print('some function')

@sample_decorator
def another_function():
	print('another function')

@sample_decorator_with_parameter("sample_param")
def another_function_sample_decorator_with_parameter():
	print("another_function_sample_decorator_with_parameter")

def main():
	some_function()
	another_function()

if __name__ == '__main__':
	main()