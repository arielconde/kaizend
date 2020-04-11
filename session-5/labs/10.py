import requests
from time import sleep
from IPython import embed
import random

BASE_URL = 'http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com'
PAGES = ['group1/1.html', 'group1/2.html',
'group1/3.html','group1/4.html', 'group1/5.html',]

def delay(seconds):
	print(f"Sleeping for {seconds} seconds")
	sleep(seconds)

def extract_html_content(target_url):
	response = requests.get(target_url)
	return response.text

def extrat_target_value_from_page(html_string):
	return ""

def get_random_int():
	return random.randint(1, 3)

def main():
	for page in PAGES:
		delay(get_random_int())
		target_page = BASE_URL + '/' + page
		print(target_page)

if __name__ == "__main__":
	main()