import openai
import os


api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


def chat_bot(content):
    print('Fetching data...')
    chat = openai.ChatCompletion.create (
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": content}
            ]
    )
    
    get_content = chat.to_dict_recursive()
    content = get_content['choices'][0]['message']['content'].strip()

    return f'\n{content}\n'    
