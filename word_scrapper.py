import requests

#PAGE_URL = 'http://94.237.55.163:43977'
PAGE_URL = 'https://api.github.com/'
resp = requests.get(PAGE_URL)
print(resp.status_code)

if resp.status_code != 200:
    print(f"{resp.status_code} received, but 200 was expected. Exiting")
    exit(1)

html_str = resp.content.decode()
print(html_str)
