import requests
from bs4 import BeautifulSoup

def get_soup() -> BeautifulSoup:
    url: str = "https://www.bbc.com/news"
    headers: dict = {'User-Agent': 'MozMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36illa/5.0'}
    response = requests.get(url, headers=headers)
    html: bytes = response.content

    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: list[str] = []
    for h in soup.find_all('h2', class_='sc-fa814188-3'):
        headline: str = h.contents[0].lower()
        headlines.append(headline)

    return sorted(headlines)
        # print(headline.text.strip())

def check_headlines(headlines: list[str], term: str):
    terms_list: list[str] = []
    terms_found: int = 0
    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline.split():
            terms_found += 1
            terms_list.append(headline)
            print(f'{i}: {headline.capitalize()} <-------------------- "{term}"')
        else:
            print(f'{i}: {headline.capitalize()}')

    print('----------------------------------')
    if terms_found:
        print(f'"{term}" was mentioned {terms_found} times.')
        print('----------------------------------')
        for i, headline in enumerate(terms_list, start=1):
            print(f'{i}: {headline.capitalize()}')
    else:
        print(f'"{term}" was not mentioned.')

def main():
    soup = get_soup()
    headlines = get_headlines(soup)
    term = input('What term would you like to search for?: >> ')
    check_headlines(headlines, term)

if __name__ == '__main__':
    main()