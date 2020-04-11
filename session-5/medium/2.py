from IPython import embed
from functools import wraps

def debug_input_and_output(func):

	@wraps(func)
	def wrapper(*args, **kwargs):
		print(f"[INPUT] ARGS: {args}")
		print(f"[INPUT] KWARGS: {kwargs}")
		output = func(*args, **kwargs)
		print(f"[OUTPUT]:", output)
		return output
	return wrapper

@debug_input_and_output
def say_something(word):
	print(word)

def main():
	say_something('Hello')

if __name__ == "__main__":
	main()