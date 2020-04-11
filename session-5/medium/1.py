from time import sleep
from functools import wraps

def delay(seconds, repitition=1):
	output = None
	def inner_function(function):
		@wraps(function)
		def wrapper(*args, **kwargs):
			print(f"[START] {function.__name__}")
			for i in range(repitition):
				print(f"Sleeping for {seconds} seconds")
				sleep(seconds)
				output = function(*args, **kwargs)
				print(f"[END] {function.__name__}")
			return output
		return wrapper
	return inner_function

@delay(seconds=2)
def say_something(word):
	print(word)

@delay(seconds=4)
def do_another_things(action):
	print("Doing:", action)

def main():
	say_something('Hello')

if __name__ == '__main__':
	main()