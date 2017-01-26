def lambda_handler(event, context):
     return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'Hello from Monzo'
            },
            'card': {
                'type': 'Simple',
                'title': 'Monzo',
                'content': 'I\'m saying hello!'
            },
            'shouldEndSession': True
        }
    }
