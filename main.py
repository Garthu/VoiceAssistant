from operacoes import *
import speech_recognition as sr
import pyttsx3

class Assistente:

    def take_command():
        command = 'Nothing'
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    print(command)
        except:
            pass
        return command

    def talk(text):
        engine.say(text)
        print(text)
        engine.runAndWait()

    def main():
        while True:
            command = Assistente.take_command()
            print(command)
            if 'play' in command:
                video = TocaVideo.play(command)
                Assistente.talk('The video: ' + video + ' is currently playing')

            elif 'time' in command:
                hora = Hora.get_time(command)
                Assistente.talk('Current time is ' + hora)
            elif 'calendar' in command:
                dia = Dia.get_day(command)
                Assistente.talk(dia)
            elif 'search' in command:
                info = Search.wikipedia_search(command)
                Assistente.talk(info)
            elif 'joke' in command:
                joke = Joke.make_a_joke(command)
                Assistente.talk(joke)
            elif 'send message' in command:
                mensagem = SendMessage.send_message(command)
                Assistente.talk("The message: " + mensagem + " is sent")
            elif 'who are you' in command:
                Assistente.talk("Hello my name is Alexa your personal Assistant")
            elif 'translate' in command:
                traducao = Translate.translate_phrase(command)
                Assistente.talk(traducao)
            elif 'break' in command:
                exit()
            else:
                Assistente.talk("Please say the command again.")
        
        

if __name__ == '__main__':
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    Assistente.main()
