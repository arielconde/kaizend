from bs4 import BeautifulSoup
import requests
import re

BASE_URL = "https://sample-target-bucket-with-html-pages.s3-ap-southeast-1.amazonaws.com/group3/target.html"

def debug_input_output(function):
	def wrapper(*args, **kwargs):
		print(f"[START: {function.__name__}]")
		output = function(*args, *kwargs)
		print(f"[END: {function.__name__}]")
		return output
	return wrapper

def extract_html_content(target_url):
	print(f"Downloading {target_url}")
	response = requests.get(target_url)
	return response.text

def extract_target_list_from_page(html_string):
	soup = BeautifulSoup(html_string, 'html.parser')
	target_list = soup.find_all('li')
	return [re.sub(r" +", " ", target.get_text().replace("\n", "")) for target in target_list]


def main():
	html_content = extract_html_content(BASE_URL)
	target_list = extract_target_list_from_page(html_content)

	for item in target_list:
		print(item, "\n")


if __name__ == "__main__":
	main()

