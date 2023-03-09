import requests
import os
from random import choice


def random_quotes():
    category = [
        'inspirational', 'faith', 'life', 'success'
        'dreams', 'imagination', 'learning', 'medical'
    ]

    # choose a random category
    random_category = choice(category)
    quote_url = f'https://api.api-ninjas.com/v1/quotes?category={random_category}'
    quote = requests.get(
        quote_url, headers={'X-Api-Key': os.getenv('API_NINJAS_KEY')})

    if quote.status_code == requests.codes.ok:
        for text in quote.json():
            return f'''\n"{text['quote']}"\n\t-{text['author']}\n'''
    else:
        print('An error occurred while retrieving the quote... Please try again')
