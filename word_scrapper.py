import requests
from bs4 import BeautifulSoup
import re
import click


def get_html_of(url):
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f"{resp.status_code} received, but 200 was expected. Exiting")
        exit(1)

    html_str = resp.content.decode()
    return html_str


def count_occurrences_in(word_list, min_length):
    word_count = {}

    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            current_count = word_count.get(word)
            word_count[word] = current_count + 1
    return word_count


#PAGE_URL = 'http://94.237.55.163:43977'


def get_all_words_from(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    all_words = re.findall(r'\w+', raw_text)
    return all_words


def get_top_words_from(all_words, min_length):
    occurrences = count_occurrences_in(all_words, min_length)
    top_words = sorted(occurrences.items(), key=lambda item: item[1], reverse=True)
    return top_words


@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL of webpage to extract from')
@click.option('--length', '-l', default=0, help='Minimum Word Length (Default: 0, No limit).')
def main(url, length):
    the_words = get_all_words_from(url)
    top_words = get_top_words_from(the_words, length)

    for i in range(10):
        print(top_words[i][0])


if __name__ == '__main__':
    main()




#TODO Add a --output / -o argument that lets us define an output file to print to instead of the console (something like with open('path.txt', 'w') as wr: and wr.write(word)).

#TODO Add common password mutations to the output, e.g., Capitalized, lowercase, UPPERCASE, and with various bits appended like the current and recent years, random numbers or symbols, e.g., 2019, 1!, 2!, 3!, 01, 123. Summer2021! and similar variations are depressingly frequent passwords.

#TODO Add a --depth / -d argument specifying the crawl depth of the script. This implies the ability to grab not only words but also URLs on the webpage(s), check if they are within scope (e.g., domain), and add them to a list of pages to crawl next.

#TODO The program currently crashes if a minimum length of 10 or higher is specified. Try to figure out why and fix it (hint: check out that last for-loop).




