import requests
from bs4 import BeautifulSoup
import re




#PAGE_URL = 'http://94.237.55.163:43977'
PAGE_URL = 'https://api.github.com/'

def get_html_of(url):
    resp = requests.get(PAGE_URL)

    if resp.status_code != 200:
        print(f"{resp.status_code} received, but 200 was expected. Exiting")
        exit(1)

    html_str = resp.content.decode()
    return html_str


html = get_html_of(PAGE_URL)
soup = BeautifulSoup(html, 'html.parser')
raw_text = soup.get_text()
print(raw_text)
all_words = re.findall(r'\w+', raw_text)
print(all_words)

word_count = {}

for word in all_words:
    if word not in word_count:
        word_count[word] = 1
    else:
        current_count = word_count.get(word)
        word_count[word] = current_count + 1

top_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
print(top_words)

#TODO convert it into a function

