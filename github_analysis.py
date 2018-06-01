import pygal
import requests
from urllib.parse import urlparse


# Add your Github API key here!
GITHUB_API_KEY = ''
URL = 'https://api.github.com/repos/pallets/flask/contributors'
HEADERS = {'Authorization': 'token {}'.format(GITHUB_API_KEY)}


def gen_next_links(headers_link_str):
    next_page_str, last_page_str = headers_link_str.split(',')
    next_page_link = next_page_str.split(';')[0][1:-1]
    link_base = next_page_link[:-1]
    start_idx = int(urlparse(next_page_link).query.split('=')[1])
    last_page_link = last_page_str.split(';')[0][2:-1]
    end_idx = int(urlparse(last_page_link).query.split('=')[1])
    return [link_base + str(idx) for idx in range(start_idx, end_idx + 1)]


def create_plot(contributors):
    chart = pygal.Bar(x_label_rotation=80, show_legend=False, spacing=170,
                      height=1000, width=4000)
    chart.title = 'Contributions to Flask on GitHub'

    names, no_contrib, _ = zip(*contributors)

    values = []
    for label, value, link in contributors:
        s_dict = {'value': value, 'label': label, 'xlink': {'href': link}}
        values.append(s_dict)

    chart.x_labels = names
    chart.add('', values)
    chart.render_to_file('contrib_flask.svg')


def make_me():
    contributors = []
    r = requests.get(URL, headers=HEADERS)

    next_urls = gen_next_links(r.headers['Link'])
    for next_url in next_urls:
        r = requests.get(next_url, headers=HEADERS)
        contributors += [(contrib['login'], contrib['contributions'],
                          contrib['html_url']) for contrib in r.json()]

    print(f'There are {len(contributors)} contributors to Flask.')
    create_plot(contributors)


if __name__ == '__main__':
    make_me()