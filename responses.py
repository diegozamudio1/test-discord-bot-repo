import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hola':
        return 'Que pasa, wey!'

    if p_message == '/roll':
        return str(random.randint(1, 100))

    if p_message == 'diego':
        return "He's so awesome!"

    if p_message == '!help':
        return "`This is a help message that you can modify.`"