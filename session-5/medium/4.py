import requests
from time import sleep
from IPython import embed
import random
from contextlib import contextmanager
from bs4 import BeautifulSoup

BASE_URL = 'http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com'
PAGES = ['group1/1.html', 'group1/2.html',
'group1/3.html','group1/4.html', 'group1/5.html',]

def debug_input_output(function):
	def wrapper(*args, **kwargs):
		print(f"[START: {function.__name__}]")
		output = function(*args, *kwargs)
		print(f"[END: {function.__name__}]")
		return output
	return wrapper

@debug_input_output
def delay(seconds):
	print(f"Sleeping for {seconds} seconds")
	sleep(seconds)

@debug_input_output
def extract_html_content(target_url):
	print(f"Downloading {target_url}")
	response = requests.get(target_url)
	return response.text

@debug_input_output
def extrat_target_value_from_page(html_string):
	soup = BeautifulSoup(html_string, "html.parser")
	div_elements = soup.find_all("div", {"id": "target"})
	return div_elements

def get_random_int():
	return random.randint(1, 3)

def main():
	for page in PAGES:
		target_page = BASE_URL + '/' + page
		html_content = extract_html_content(target_page)
		print(html_content)

		target_values = extrat_target_value_from_page(html_content)
		for target_value in target_values:
			print(target_value.get_text())

		delay(get_random_int())


if __name__ == "__main__":
	main()