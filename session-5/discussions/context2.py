from contextlib import contextmanager

@contextmanager
def block(label):
	print(f"START: {label}")
	yield
	print(f"END: {label}")

def main():
	with block("task 1"):
		with block("task 2"):
			print("inside task 1")

if __name__ == "__main__":
	main()