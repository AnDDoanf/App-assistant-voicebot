# import datetime
# import webbrowser
# import wikipedia
# import wolframalpha
from tell import get_joke, get_pickup
from Assistant import Assistant

class AssistantBot():
    def run(self):
        bot = Assistant()
        bot.speak('I am waking up.')
        while True:
            query = bot.parseCommand().lower().split()
            if query[0] in bot.activationWord:
                if query[0] == 'assistant': query.pop(0)

                if query[0] == 'say':
                    if 'hello' in query:
                        bot.speak('Hello, I am your AI assistant, I can do nothing right now but speak. Nice to meet you.')
                    else: 
                        query.pop(0)
                        speech = ' '.join(query)
                        bot.speak(speech) 

                if query[0] == 'tell':
                    if 'joke' in query:
                        bot.speak('Here it is: ' + get_joke())
                    if 'pick-up' in query or ('pick' in query and 'up' in query) :
                        bot.speak('Here it is: ' + get_pickup())
                
                if query[0] == 'what':
                    pass

                if query[0] == 'goodbye':
                    bot.speak('See you later')
                    break