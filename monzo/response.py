def build(title, output, session=True):
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            },
            'card': {
                'type': 'Simple',
                'title': title,
                'content': output
            },
            'shouldEndSession': session
        }
    }

def error():
    return build("Request error", "I'm sorry, your request could not be completed - please try again.")
