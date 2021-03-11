import speech_recognition as sr
from Dominio.GerenciaDeFuncoes.operacoes import *

class Assistente:

    def take_command():
        listener = sr.Recognizer()
        command = 'Nothing'
        try:
            with sr.Microphone() as source:
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
        except:
            pass
        return command


    def run():
        while True:
            command = Assistente.take_command()
            if 'play' in command:
                video = TocaVideo.play(command)
                return ('The video: ' + video + ' is currently playing')

            elif 'time' in command:
                hora = Hora.get_time(command)
                return ('Current time is ' + hora)

            elif 'calendar' in command:
                dia = Dia.get_day(command)
                return dia

            elif 'search' in command:
                info = Search.wikipedia_search(command)
                return info

            elif 'joke' in command:
                joke = Joke.make_a_joke(command)
                return joke

            elif 'send message' in command:
                mensagem = SendMessage.send_message(command)
                return ("The message: " + mensagem + " is sent")

            elif 'who are you' in command:
                return ("Hello my name is Alexa your personal Assistant")

            elif 'translate' in command:
                traducao = Translate.translate_phrase(command)
                return traducao

            elif 'break' in command:
                exit()
            else:
                return ("Please say the command again.")