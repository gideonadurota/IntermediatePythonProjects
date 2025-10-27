import pyshorteners


def shorten_url(url: str) -> str:
    if url.startswith('http'):
        split_url = url.split(':')
        split_url[0] = "https"
        url = ":".join(split_url)

    if not url.startswith('https') or not url.startswith('http'):
        url = "https://" + url
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        return short_url
    except Exception as e:
        raise Exception(f"Failed to shorten URL: {e}")

def main():
    user_input = input('Enter the url to shorten: ')
    shortened_url = shorten_url(user_input)
    print(shortened_url)

if __name__ == '__main__':
    main()

