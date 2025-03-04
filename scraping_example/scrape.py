import requests
from bs4 import BeautifulSoup
import pprint


def get_page_data(page_number=None):
    base_url = 'https://news.ycombinator.com/news'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.titleline')
    subtext = soup.select('.subtext')
    if page_number:
        i = 2
        while i <= page_number:
            url = base_url + f'?p={i}'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links += soup.select('.titleline')
            subtext += soup.select('.subtext')
            i += 1
    data = {'links': links, 'subtext': subtext}
    return data


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(data):
    links = data['links']
    subtext = data['subtext']
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.select('a')[0].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(get_page_data(4)))
