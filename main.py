import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def count_clicks(token, link):

    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = {'units': '-1'}
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary',
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()["total_clicks"]


def shorten_link(token, url):

    headers = {
        'Authorization': f'Bearer {token}',
    }
    body = {
        'long_url': url,
    }
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json=body
    )
    response.raise_for_status()
    return response.json()['id']


def is_bitlink(token, url):

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{url}',
        headers=headers
    )
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    parser = argparse.ArgumentParser(
        description='Программа возвращает: bitlink, если ссылка bitlink:'
                    ' возвращает кол-во переходов по ней.'
    )
    parser.add_argument(
        'args',
        help='Введите полную ссылку или битлинк'
    )
    args = parser.parse_args()
    args = args.args
    parsed_args = urlparse(args)
    is_link = f"{parsed_args.netloc}{parsed_args.path}"

    try:
        if is_bitlink(bitly_token, is_link):
            cliks_count = count_clicks(bitly_token, is_link)
            print('Переходов по bitlink:', cliks_count)
        else:
            bitlink = shorten_link(bitly_token, args)
            print('bitlink:', bitlink)
    except requests.exceptions.HTTPError as err:
        print("Ошибка", err)


if __name__ == "__main__":
    main()


