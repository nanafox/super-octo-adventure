import requests
import os
from random import choice


def random_quotes(user_category=None):
    """
    Generates a random quote based on the predefined categories
    
    :params: user_category. Default value is None.
             A random category is generated if not specified
    :returns: None if an error occurred. Sometimes the request seems to return nothing.
              This also the return value to be None.
    """
    
    category = [
        'inspirational', 'faith', 'life', 'success'
        'dreams', 'imagination', 'learning', 'medical'
    ]

    if user_category is not None:
        # set category to user's choice
        random_category = user_category
    else:
        # choose a random category 
        random_category = choice(category)
    
    quote_url = f'https://api.api-ninjas.com/v1/quotes?category={random_category}'
    try:
        quote = requests.get(
            quote_url, headers={'X-Api-Key': os.getenv('API_NINJAS_KEY')})
    except requests.ConnectionError:
        return '\nERROR: Please check your internet connection and try again.'
        
    else:    
        if quote.status_code == requests.codes.ok:
            for text in quote.json():
                return f'''\n"{text['quote']}"\n\t- {text['author']} ({text['category'].capitalize()})\n'''
        
        return 'An error occurred while retrieving the quote... Please try again'
    