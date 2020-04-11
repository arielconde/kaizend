from contextlib import contextmanager

class Job():
	def __init__(self, label):
		self.label = label
		self.target_url = None
		self.selector = None
		self.save_file = None

	def perform(self):
		pass


@contextmanager
def scraping_job(label):
	print(f'[START {label}]')
	job = Job(label)
	yield(job)
	print_job(job)
	print(f'[END {label}]')


def print_job(job):
	print("TARGET_URL", job.target_url)
	print("SELECTOR", job.selector)
	print("SAVE_FILE", job.save_file)

def main():
	with scraping_job('Job 1') as job:
		job.target_url = "<url 1>"
		job.selector = "<selector 1>"
		job.save_file = "<filename_1>"

	with scraping_job('Job 2') as job:
		job.target_url = "<url 2>"
		job.selector = "<selector 2>"
		job.save_file = "<filename_2>"

if __name__ == "__main__":
	main()