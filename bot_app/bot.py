from chat_bot import chat_bot
from quotes_bot import random_quotes

capabilities = {
    'help answer your questions': '/ask',
    'give you a random quote in almost in any category': '/quote',
}

def start_bot():
    running = True
    def show_capabilities():
        print("Here's a list of what I can do. I could")
        for what, how in capabilities.items():
            print(f'\t- {what.capitalize()}. Use {how} to prompt me')
        print('\t- Use /quit to end the session')
        
        start_bot()

    while running:
        try:
            prompt = input('\n(Use /show to list my capabilities)\nHow can I help?: ')
            if prompt in capabilities.values():
                if prompt == '/ask':
                    print(chat())
                if prompt == '/quote':
                    print(random_quotes())
                    
            elif prompt == '/quit':
                print('Have a nice day...')
                quit(0)
                
            else:
                show_capabilities()
        except EOFError:
            print("\nCtrl_D received")
            quit(0)
        except KeyboardInterrupt:
            print()
            quit(1)
            
        
def chat():
    try:
        ask = input("Ask a question: ")
        if ask.lower() == 'quit':
            print('Have a nice day!')
            quit()
    
    except KeyboardInterrupt:
        quit()
    except EOFError:
        quit()
        
    chat_response = chat_bot(ask)

    return chat_response


if __name__ == '__main__':
    start_bot()
